Script ini digunakan untuk melakukan proses ELT (Extract, Load, Transform) sederhana dari database MySQL ke PostgreSQL menggunakan Python dengan bantuan pustaka pandas dan sqlalchemy.

# 🔧 Teknologi yang Digunakan
- Python
- Pandas
- SQLAlchemy
- dotenv
- MySQL
- PostgreSQL
- Docker 

# ⚙️ Konfigurasi Lingkungan

Sebelum menjalankan script ini, pastikan kamu sudah membuat file .env dengan variabel berikut:

```
MYSQL_ROOT_PASSWORD=your_mysql_password
MYSQL_DATABASE=your_mysql_database_name

POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_database_name
```

# 🚀 Cara Kerja Script

- Load Konfigurasi

    Mengambil variabel lingkungan dari file .env.

- Koneksi Database

    Membuat koneksi ke MySQL dan PostgreSQL menggunakan sqlalchemy.

- Extract

    Mengambil data dari tabel store dan trx_total di MySQL.

- Transform

    Memastikan kolom trx_amount bertipe numerik (int64).

- Load

    Mengirim (overwrite/replace) tabel store dan trx_total ke PostgreSQL.

# ▶️ Cara Menjalankan

Aktifkan environment, lalu jalankan perintah berikut:
```
python elt_pipeline.py
```

Jika berhasil, akan muncul output:
```
ELT berhasil!
```

