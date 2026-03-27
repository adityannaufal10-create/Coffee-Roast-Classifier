import os
import torch
import torch.nn as nn
from flask import Flask, request, jsonify, render_template
from torchvision import transforms
from PIL import Image
import timm
import io
import numpy as np
import random

def set_seed(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
app = Flask(__name__)

# --- JALUR KE FILE OTAK ---
MODEL_PATH = "model/best_EfficientNet-B0.pth"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- KAMUS PENERJEMAH (Kaggle -> JavaScript) ---
KAGGLE_CLASSES = ["Dark", "Green", "Light", "Medium"]
FRONTEND_CLASSES = {
    "Dark": "Dark Roast",
    "Green": "Green",
    "Light": "Light Roast",
    "Medium": "Medium Roast"
}

# --- ARSITEKTUR KAGGLE (Biar akurat 100%) ---
class CoffeeClassifier(nn.Module):
    def __init__(self, backbone_name="efficientnet_b0", feat_dim=1280, num_classes=4):
        super().__init__()
        self.backbone = timm.create_model(backbone_name, pretrained=False, num_classes=0)
        self.head = nn.Sequential(
            nn.LayerNorm(feat_dim), nn.Dropout(0.3),
            nn.Linear(feat_dim, 256), nn.GELU(),
            nn.Dropout(0.2), nn.Linear(256, num_classes),
        )
    def forward(self, x):
        return self.head(self.backbone(x))

model = CoffeeClassifier()
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE), strict=True)
model.to(DEVICE).eval()

# --- TRANSFORM (Konsisten & Kaku) ---
data_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    set_seed(42)
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file'}), 400
    
    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        tensor = data_transform(image).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
            output = model(tensor)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            confidence, predicted = torch.max(probabilities, 0)

        # Terjemahkan nama pemenang ke bahasa Frontend
        kaggle_winner = KAGGLE_CLASSES[predicted.item()]
        frontend_winner = FRONTEND_CLASSES[kaggle_winner]

        # Siapkan rapor nilai dengan nama kelas Frontend
        all_scores_dict = {}
        for i, k_class in enumerate(KAGGLE_CLASSES):
            f_class = FRONTEND_CLASSES[k_class]
            all_scores_dict[f_class] = float(probabilities[i].item() * 100)

        # FORMAT SPESIFIK SESUAI KODE JAVASCRIPT KAMU
        return jsonify({
            'success': True,
            'result': {
                'label': frontend_winner,
                'confidence': float(confidence.item() * 100),
                'all_scores': all_scores_dict
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)