from fastapi import FastAPI
import os
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()
# 
app = FastAPI()

# Koneksi ke PostgreSQL
PG_USER = os.getenv("POSTGRES_USER")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD")
PG_DB = os.getenv("POSTGRES_DB")
USE_DOCKER = os.getenv("USE_DOCKER", "false").lower() == "true"

pg_url = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    username=PG_USER,
    password=PG_PASSWORD,
    host="postgres"     ,
    port=5432 ,
    database=PG_DB
)

pg_engine = sqlalchemy.create_engine(pg_url)


@app.get("/transaction-detail")
def get_transaction_detail():
    query = """
    SELECT
        trx.trx_id,
        trx.store_id,
        trx.customer_id,
        trx.trx_amount,
        s.store_name,
        s.store_format_name,
        s.store_city,
        s.store_state
    FROM trx_total trx
    JOIN store s ON trx.store_id = s.store_id
    """
    df = pd.read_sql(query, pg_engine)
    return df.to_dict(orient="records")


@app.get("/store-detail")
def get_store_detail():
    query = """
    SELECT
        s.store_name,
        s.store_format_name,
        s.store_city,
        s.store_state,
        SUM(trx.trx_amount) AS amount
    FROM trx_total trx
    JOIN store s ON trx.store_id = s.store_id
    GROUP BY s.store_name, s.store_format_name, s.store_city, s.store_state
    """
    df = pd.read_sql(query, pg_engine)
    return df.to_dict(orient="records")


@app.get("/customer-detail")
def get_customer_detail():
    query = """
    SELECT
        trx.customer_id,
        SUM(trx.trx_amount) AS amount,
        STRING_AGG(DISTINCT s.store_name, ', ') AS stores
    FROM trx_total trx
    JOIN store s ON trx.store_id = s.store_id
    GROUP BY trx.customer_id
    """
    df = pd.read_sql(query, pg_engine)
    return df.to_dict(orient="records")
