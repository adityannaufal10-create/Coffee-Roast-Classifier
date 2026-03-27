# Gunakan komputer Python versi 3.9
FROM python:3.9

# Bikin folder kerja di dalam server
WORKDIR /code

# Copy daftar belanjaan dan install
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy semua file kamu (termasuk folder model dan templates)
COPY . .

# Buka gerbang 7860
EXPOSE 7860

# Perintah untuk menyalakan website
CMD ["python", "app.py"]