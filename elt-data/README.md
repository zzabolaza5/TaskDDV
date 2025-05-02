Script ini digunakan untuk melakukan proses ELT (Extract, Load, Transform) sederhana dari database MySQL ke PostgreSQL menggunakan Python dengan bantuan pustaka pandas dan sqlalchemy.

🔧 Teknologi yang Digunakan
- Python
- Pandas
- SQLAlchemy
- dotenv
- MySQL
- PostgreSQL
- Docker 

⚙️ Konfigurasi Lingkungan
Sebelum menjalankan script ini, pastikan kamu sudah membuat file .env dengan variabel berikut:

```
MYSQL_ROOT_PASSWORD=your_mysql_password
MYSQL_DATABASE=your_mysql_database_name

POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_database_name
```