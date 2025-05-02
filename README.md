# 🧩 ELT Retail Data Pipeline & API (TASK DDV)

Proyek ini mencakup ETL/ELT pipeline menggunakan Python, Docker, dan PostgreSQL, serta penyediaan REST API menggunakan FastAPI untuk mengakses data transaksi dan toko.

# 📌 Tujuan

Ekstrak data transaksi retail dari database MySQL

Load dan transform ke PostgreSQL

Sediakan API untuk menampilkan informasi transaksi, toko, dan pelanggan

# ⚙️ Teknologi yang Digunakan

- Python 3.10
- MySQL 8.0
- PostgreSQL 14
- Pandas & SQLAlchemy
- FastAPI
- Docker & Docker Compose 28.0.4

# 📌 Running Program

1. Clone Repository
```
git clone https://github.com/zzabolaza5/TaskDDV.git
cd TaskDDV
```

2. Siapkan .env
```
MYSQL_ROOT_PASSWORD=mysqlpass
MYSQL_DATABASE=task_DDV

POSTGRES_USER=postgres
POSTGRES_PASSWORD=pgpass
POSTGRES_DB=store_trx_DDV

USE_DOCKER=true
```

3. Jalankan dengan Docker Compose
```
docker-compose up --build
```

Ini akan:
- Membuat container untuk MySQL dan PostgreSQL
- Mengisi MySQL dengan dummy data (dummy_data.sql)
- Menjalankan ETL pipeline (elt_pipeline.py) untuk mentransfer ke PostgreSQL
- Menjalankan FastAPI REST API

# 🔁 ELT Pipeline
# 📄 File: elt-data/elt_pipeline.py

- Extract data dari MySQL: tabel store dan trx_total
- Transform data (konversi trx_amount ke tipe numerik)
- Load ke PostgreSQL dalam bentuk tabel yang sama
```
cd elt-data
python elt_pipeline.py
```

# 🌐 REST API
# 📄 File: task-api/main.py

Endpoint:
| Endpoint              | Method | Deskripsi                                 |
| --------------------- | ------ | ----------------------------------------- |
| `/transaction-detail` | GET    | Detail transaksi dan toko                 |
| `/store-detail`       | GET    | Total transaksi per toko                  |
| `/customer-detail`    | GET    | Total transaksi per pelanggan & toko-toko |

TASK

1. Create ELT data pipeline from MySQL to PostgreSQL ✅

2. Create API for consuming the processed data
- get transaction detail payload: trx_id, store_id, customer_id, trx_amount, store_name, store_format_name, store_city, store_state ✅
- get store detail payload: store_name, store_format_name, store_city, store_state, amount ✅ 
- get customer detail payload: customer_id, amount, stores ✅ 