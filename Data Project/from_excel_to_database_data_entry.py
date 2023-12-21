import pandas as pd
import psycopg2
import logging
from config import database_name, user, password, host, port, file_path1, table_name1, file_path2, table_name2


logging.basicConfig(filename='proje_log.log', level=logging.INFO)

def import_excel_to_postgresql(excel_path, table_name):
    try:
        df = pd.read_excel(excel_path, engine='openpyxl')
        conn = psycopg2.connect(
            dbname=database_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()
        for _, row in df.iterrows():
            values = []
            for value in row:
                if pd.isna(value):
                    values.append('NULL')
                else:
                    values.append(f"'{value}'")
            values_str = ",".join(values)
            query = f"INSERT INTO {table_name} VALUES ({values_str})"
            cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        logging.info(f"Veriler {table_name} tablosuna başarıyla PostgreSQL'e aktarıldı.")
    except Exception as hata:
        logging.error(f'Hata: {hata}')
        print("Hata:", hata)


import_excel_to_postgresql(file_path1, table_name1)
