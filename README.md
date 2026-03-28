# ☕ Coffee Roast Classifier

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange)
![EfficientNet-B0](https://img.shields.io/badge/Backbone-EfficientNet--B0-red)
![Deployment](https://img.shields.io/badge/Deploy-Hugging%20Face%20Spaces-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> Aplikasi Computer Vision berbasis Deep Learning untuk mengklasifikasikan tingkat roasting kopi secara otomatis menggunakan gambar.

Coba aplikasi live:  
https://huggingface.co/spaces/adityanaufal/Coffee-Roast-Classifier

Link Kaggle dataset sebelum gambar dikonversi:
https://www.kaggle.com/datasets/sot2542/coffee-bean-dataset-v2

Link dataset setelah gambar dikonversi:
https://drive.google.com/file/d/1nyIBdJgtEbo7UYdeDhsu8VcNUUlqO5Rq/view?usp=sharing

---

## Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Latar Belakang](#latar-belakang)
- [Fitur Utama](#fitur-utama)
- [Kelas Klasifikasi](#kelas-klasifikasi)
- [Arsitektur Sistem](#arsitektur-sistem)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Repository](#struktur-repository)
- [Alur Kerja Aplikasi](#alur-kerja-aplikasi)
- [Instalasi](#instalasi)
- [Menjalankan Secara Lokal](#menjalankan-secara-lokal)
- [Menggunakan Docker](#menggunakan-docker)
- [Deployment](#deployment)
- [API Endpoint](#api-endpoint)
- [Format Respons](#format-respons)
- [Preprocessing Gambar](#preprocessing-gambar)
- [Detail Model](#detail-model)
- [Troubleshooting](#troubleshooting)
- [Pengembangan Lanjutan](#pengembangan-lanjutan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Author](#author)
- [Ucapan Terima Kasih](#ucapan-terima-kasih)

---

## Tentang Proyek

**Coffee Roast Classifier** adalah aplikasi web berbasis machine learning yang digunakan untuk memprediksi tingkat roasting biji kopi dari sebuah gambar.  
Aplikasi ini menerima input berupa citra kopi, memproses gambar tersebut, lalu mengembalikan hasil prediksi kelas roasting beserta confidence score dan probabilitas untuk setiap kelas.

Proyek ini dibangun menggunakan:
- **Flask** sebagai web framework,
- **PyTorch** sebagai framework deep learning,
- **EfficientNet-B0** sebagai backbone model,
- **Docker** untuk kemudahan deployment,
- serta dapat dijalankan di **Hugging Face Spaces**.

---

## Latar Belakang

Roasting kopi merupakan salah satu tahap penting yang menentukan aroma, warna, rasa, dan karakter akhir biji kopi.  
Perbedaan tingkat roasting dapat terlihat dari warna visual biji kopi, sehingga computer vision dapat dimanfaatkan untuk membantu proses identifikasi secara otomatis.

Dengan pendekatan deep learning, proses klasifikasi dapat dilakukan secara:
- lebih cepat,
- lebih konsisten,
- dan lebih mudah diintegrasikan ke aplikasi web.

Proyek ini menunjukkan implementasi praktis klasifikasi citra menggunakan model convolutional berbasis EfficientNet.

---

## Fitur Utama

- Upload gambar kopi langsung melalui antarmuka web
- Klasifikasi otomatis tingkat roasting
- Menampilkan label hasil prediksi
- Menampilkan confidence score prediksi
- Menampilkan probabilitas untuk seluruh kelas
- Mendukung inferensi lokal
- Siap dijalankan menggunakan Docker
- Siap deploy ke Hugging Face Spaces
- Struktur kode sederhana dan mudah dikembangkan

---

## Kelas Klasifikasi

Model dilatih untuk mengenali **4 kelas utama**:

1. **Green Bean**  
   Biji kopi mentah / belum melalui proses roasting.

2. **Light Roast**  
   Tingkat roasting ringan dengan warna lebih terang.

3. **Medium Roast**  
   Tingkat roasting menengah, seimbang antara aroma dan warna.

4. **Dark Roast**  
   Tingkat roasting gelap dengan warna lebih pekat.

Pada implementasi frontend, label kelas ditampilkan sebagai:
- `Green`
- `Light Roast`
- `Medium Roast`
- `Dark Roast`

---

## Arsitektur Sistem

Secara umum, sistem terdiri dari beberapa bagian:

### 1. Input Gambar
Pengguna mengunggah gambar kopi melalui halaman web.

### 2. Preprocessing
Gambar diubah menjadi format yang sesuai dengan model:
- resize,
- center crop,
- konversi ke tensor,
- normalisasi.

### 3. Inferensi Model
Tensor gambar dimasukkan ke model EfficientNet-B0 yang telah dilatih.

### 4. Softmax
Output model diubah menjadi probabilitas untuk setiap kelas.

### 5. Hasil Prediksi
Kelas dengan probabilitas tertinggi ditampilkan sebagai hasil akhir.

---

## Teknologi yang Digunakan

### Backend
- Python
- Flask

### Deep Learning
- PyTorch
- Torchvision
- timm

### Image Processing
- Pillow (PIL)
- NumPy

### Deployment
- Docker
- Hugging Face Spaces

### Frontend
- HTML
- CSS
- JavaScript

---

## Struktur Repository

Struktur repository yang digunakan pada proyek ini terdiri dari:

```bash
Coffee-Roast-Classifier/
├── app.py
├── Dockerfile
├── requirements.txt
├── model/
│   └── best_EfficientNet-B0.pth
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   └── index.html
└── README.md
```

### Penjelasan Folder/File
- **app.py**  
  File utama aplikasi Flask yang memuat model, preprocessing, dan endpoint prediksi.

- **model/**  
  Folder penyimpanan file model hasil training.

- **templates/**  
  Folder untuk file HTML frontend.

- **static/**  
  Folder aset statis seperti CSS, JavaScript, dan gambar.

- **Dockerfile**  
  Konfigurasi container untuk deployment.

- **requirements.txt**  
  Daftar dependensi Python yang dibutuhkan.

---

## Alur Kerja Aplikasi

Berikut alur kerja aplikasi dari awal hingga menghasilkan prediksi:

1. Pengguna membuka halaman utama.
2. Pengguna mengunggah gambar kopi.
3. Server menerima file gambar melalui endpoint `/predict`.
4. Gambar dibaca menggunakan PIL.
5. Gambar diproses dengan transformasi yang konsisten.
6. Gambar diubah menjadi tensor dan dikirim ke device yang tersedia.
7. Model menghasilkan logits.
8. Softmax digunakan untuk menghitung probabilitas kelas.
9. Kelas dengan probabilitas tertinggi dipilih.
10. Hasil prediksi dikirim kembali ke frontend dalam format JSON.

---

## Instalasi

### 1. Clone repository
```bash
git clone https://github.com/adityannaufal10-create/Coffee-Roast-Classifier.git
cd Coffee-Roast-Classifier
```

### 2. Buat virtual environment
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Menjalankan Secara Lokal

Setelah semua dependensi terpasang, jalankan aplikasi dengan:

```bash
python app.py
```

Aplikasi akan berjalan pada:

```bash
http://127.0.0.1:7860
```

Jika dijalankan pada server/container, aplikasi menggunakan:
- host: `0.0.0.0`
- port: `7860`

---

## Menggunakan Docker

Proyek ini juga dapat dijalankan melalui Docker agar proses deployment lebih mudah dan konsisten.

### Build image
```bash
docker build -t coffee-roast-classifier .
```

### Jalankan container
```bash
docker run -p 7860:7860 coffee-roast-classifier
```

Setelah container aktif, buka:

```bash
http://127.0.0.1:7860
```

---

## Deployment

Repository ini disiapkan untuk deployment container-based.  
Pada konfigurasi Docker, aplikasi:

- menginstal dependensi dari `requirements.txt`,
- menyalin seluruh isi repository,
- membuka port `7860`,
- lalu menjalankan `python app.py`.

Deploy yang tersedia di Hugging Face Spaces memanfaatkan konfigurasi yang sama sehingga perilaku aplikasi tetap konsisten antara lokal dan produksi.

---

## API Endpoint

### `GET /`
Menampilkan halaman utama aplikasi web.

### `POST /predict`
Menerima file gambar dan mengembalikan hasil klasifikasi.

#### Request
- Method: `POST`
- Content-Type: `multipart/form-data`
- Field file: `file`

#### Contoh request menggunakan cURL
```bash
curl -X POST http://127.0.0.1:7860/predict   -F "file=@sample.jpg"
```

---

## Format Respons

### Respons sukses
```json
{
  "success": true,
  "result": {
    "label": "Medium Roast",
    "confidence": 95.42,
    "all_scores": {
      "Dark Roast": 1.21,
      "Green": 0.34,
      "Light Roast": 2.03,
      "Medium Roast": 95.42
    }
  }
}
```

### Respons error
```json
{
  "success": false,
  "error": "pesan error"
}
```

---

## Preprocessing Gambar

Sebelum gambar masuk ke model, pipeline preprocessing yang digunakan adalah:

- `Resize(256)`
- `CenterCrop(224)`
- `ToTensor()`
- `Normalize(mean, std)`

Nilai normalisasi yang digunakan:
- mean: `[0.485, 0.456, 0.406]`
- std: `[0.229, 0.224, 0.225]`

Pipeline ini umum digunakan pada model backbone berbasis ImageNet agar input konsisten dengan format pelatihan.

---

## Detail Model

### Backbone
Model menggunakan **EfficientNet-B0** sebagai backbone feature extractor.

### Head Klasifikasi
Bagian klasifikasi di atas backbone terdiri dari:

- LayerNorm
- Dropout
- Linear layer
- Aktivasi GELU
- Dropout
- Linear output layer

### Device
Model akan menggunakan:
- `cuda` jika GPU tersedia,
- `cpu` jika GPU tidak tersedia.

### Reproducibility
Aplikasi menerapkan seed agar hasil inferensi lebih konsisten:
- Python `random`
- NumPy
- PyTorch
- CUDA deterministic mode

---

## Parameter Penting di `app.py`

Beberapa konfigurasi utama yang digunakan:

- **MODEL_PATH**  
  Lokasi file model:
  ```python
  model/best_EfficientNet-B0.pth
  ```

- **KAGGLE_CLASSES**  
  Urutan label kelas internal model:
  ```python
  ["Dark", "Green", "Light", "Medium"]
  ```

- **FRONTEND_CLASSES**  
  Pemetaan label internal ke label yang ditampilkan ke pengguna.

- **Port aplikasi**  
  ```python
  port=7860
  ```

---

## Troubleshooting

### 1. Model tidak ditemukan
Pastikan file model tersedia pada path berikut:

```bash
model/best_EfficientNet-B0.pth
```

### 2. Dependency error
Pastikan seluruh library pada `requirements.txt` telah terpasang dengan benar.

### 3. Gambar tidak bisa diproses
Pastikan file yang diunggah:
- formatnya valid,
- bukan file rusak,
- dan dapat dibuka oleh PIL.

### 4. Port sudah dipakai
Jika port `7860` sudah digunakan aplikasi lain, ubah port pada `app.py` atau hentikan proses yang memakai port tersebut.

### 5. Hasil prediksi tidak stabil
Pastikan model dan preprocessing yang digunakan sesuai dengan pipeline training.

---

## Pengembangan Lanjutan

Beberapa pengembangan yang dapat ditambahkan ke proyek ini:

- menambah visualisasi confidence score,
- menampilkan top-3 prediksi,
- membuat tampilan UI yang lebih modern,
- menambahkan batch prediction,
- menambahkan logging inferensi,
- menyediakan API dokumentasi berbasis Swagger,
- menambahkan uji coba otomatis,
- membuat versi mobile-friendly,
- menambahkan evaluasi model di README.

---

## Kontribusi

Kontribusi sangat terbuka. Langkah umum:

1. Fork repository ini.
2. Buat branch baru.
3. Lakukan perubahan.
4. Commit perubahan.
5. Push ke branch.
6. Buat Pull Request.

### Contoh alur git
```bash
git checkout -b feature/nama-fitur
git add .
git commit -m "Menambahkan fitur baru"
git push origin feature/nama-fitur
```

---

## Lisensi

Repository ini dapat menggunakan lisensi **MIT** atau lisensi lain sesuai kebutuhan proyek.  
Tambahkan file `LICENSE` jika ingin mendefinisikan lisensi secara resmi.

---

## Author

Proyek ini dikembangkan oleh:

- **Aditya Naufal Jay Putra**
- **Moch Arizal**

### Profil
- GitHub Aditya: https://github.com/adityannaufal10-create
- LinkedIn Aditya: https://www.linkedin.com/in/aditya-naufal-jay-putra-78a667324
- GitHub Moch Arizal: https://github.com/arizal261104
- LinkedIn Moch Arizal: https://www.linkedin.com/in/moch-arizal/
