import pandas as pd
import psycopg2
import logging
import config

logging.basicConfig(filename='proje_log.log', level=logging.INFO)

def export_postgresql_to_excel(table_name, conn):
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)
        df.to_excel("to_account_move.xlsx", index=False)
        logging.info(f"Veri {table_name} tablosundan Excel dosyasına başarıyla yazıldı.")
    except Exception as hata:
        logging.error(f'Hata: {hata}')
        print("Hata:", hata)

conn = psycopg2.connect(
    dbname=config.database_name,
    user=config.user,
    password=config.password,
    host=config.host,
    port=config.port
)

export_postgresql_to_excel(config.table_name1, conn)

conn.close()