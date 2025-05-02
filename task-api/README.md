📦 task-api: REST API untuk Akses Data Transaksi Retail

Aplikasi ini adalah service FastAPI yang menyediakan API untuk mengakses data transaksi, toko, dan pelanggan dari database PostgreSQL hasil proses ELT.

🚀 Fitur Endpoint

| Endpoint              | Method | Deskripsi                                               |
| --------------------- | ------ | ------------------------------------------------------- |
| `/transaction-detail` | GET    | Mengembalikan seluruh data transaksi dengan detail toko |
| `/store-detail`       | GET    | Menampilkan rekap transaksi per toko                    |
| `/customer-detail`    | GET    | Menampilkan rekap transaksi per pelanggan               |

🏗️ Arsitektur Koneksi Database

Aplikasi menggunakan SQLAlchemy untuk membuat koneksi ke PostgreSQL dengan variabel lingkungan yang disimpan di .env.
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=store_trx_DDV
USE_DOCKER=true
```

▶️ Menjalankan API

Secara lokal:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Dengan Docker dan Docker Compose:

Pastikan service ini didefinisikan di docker-compose.yml, lalu jalankan:
```
docker-compose up --build
```

