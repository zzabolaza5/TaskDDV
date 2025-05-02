import os
import pandas as pd
import sqlalchemy

# load dari .env
from dotenv import load_dotenv
load_dotenv()
MYSQL_PASSWORD = os.getenv ("MYSQL_ROOT_PASSWORD")
MYSQL_DB = os.getenv ("MYSQL_DATABASE")

PG_USER = os.getenv ("POSTGRES_USER")
PG_PASSWORD = os.getenv ("POSTGRES_PASSWORD")
PG_DB = os.getenv ("POSTGRES_DB")

# koneksi ke MySQL
mysql_url = sqlalchemy.URL.create(
    drivername = "mysql+pymysql",
    username = 'root',
    password = MYSQL_PASSWORD,
    host = "mysql",
    port = 3306,
    database = MYSQL_DB
)

# koneksi ke PostgreSQL
pg_url = sqlalchemy.URL.create(
    drivername = "postgresql+psycopg2",
    username = PG_USER,
    password = PG_PASSWORD,
    host = "postgres",
    port = 5432,
    database = PG_DB
)

# buat engine
mysql_engine = sqlalchemy.create_engine(mysql_url)
pg_engine = sqlalchemy.create_engine(pg_url)

# ambil data dari MySQL
stores_df = pd.read_sql("SELECT * FROM store", mysql_engine)
trx_df = pd.read_sql("SELECT * FROM trx_total", mysql_engine)

# pastikan tipe data numerik
trx_df["trx_amount"] = trx_df["trx_amount"].astype("int64")

# kirim ke PostgreSQL
trx_df.to_sql("trx_total", pg_engine, if_exists="replace", index=False)
stores_df.to_sql("store", pg_engine, if_exists="replace", index=False)


print("ELT berhasil!")