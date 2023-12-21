import pandas as pd
import config
import logging


logging.basicConfig(filename='proje_log.log', level=logging.INFO)

def excelden_oku(dosya_yolu, sheet_name, first_row, finis_row, first_column, finish_column):
    try:
        df = pd.read_excel(dosya_yolu, sheet_name=sheet_name)
        data = df.iloc[first_row:finis_row, first_column:finish_column]
        logging.info(f"Excel dosyasından veri başarıyla okundu:\n{data}")
        return data
    except Exception as hata:
        logging.error(f'Hata: {hata}')
        print("Hata çıktısı:", hata)
        return None

dosya_yolu = config.excel_path
sheet_name = config.sheet_name
first_row = config.start_row
finis_row = config.finish_row
first_column = config.start_column
finish_column = config.finish_column
data = excelden_oku(dosya_yolu, sheet_name, first_row, finis_row, first_column, finish_column)
print(data)
