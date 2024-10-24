# Python 3.9 tabanlı bir imaj kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Flask uygulamasını çalışt
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]

