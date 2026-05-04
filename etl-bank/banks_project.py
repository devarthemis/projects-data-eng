import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import numpy as np

from datetime import datetime, timezone

# Declarando valores conhecidos
base_url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
exchange_rate = pd.read_csv("exchange_rate.csv")

attributes = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]

output_csv = 'Largest_banks_data.csv'

db_name = 'Banks.db'
table_name = 'Largest_banks'

log_file = 'code_log.txt'


def extract(base_url: str):
    df = pd.DataFrame(columns=attributes)
    soup = BeautifulSoup(requests.get(base_url).text, "lxml")

    table = soup.find_all("table")[1]
    rows = table.find_all("tr")[1::]

    bank_names = [row.find_all("td")[::][1].text.strip() for row in rows]
    capitalization = [row.find_all("td")[::][2].text.strip().replace(",", "") for row in rows]
    df["Name"] = bank_names
    df["MC_USD_Billion"] = capitalization

    return df


def transform(df: pd.DataFrame, exchange_rate: pd.DataFrame):
    usd_rate = df['MC_USD_Billion'].astype(float).to_numpy()
    exc_rate = exchange_rate['Rate'].astype(float).to_numpy()
    df['MC_GBP_Billion'] = np.round(usd_rate * exc_rate[1], 2)
    df['MC_EUR_Billion'] = np.round(usd_rate * exc_rate[0], 2)
    df['MC_INR_Billion'] = np.round(usd_rate * exc_rate[2], 2)

    return df


def load_to_csv(data: pd.DataFrame, output_csv: str):
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    return df


def load_to_db(df: pd.DataFrame):
    conn = sqlite3.connect(db_name)
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        log_progress("Dados carregados com sucesso")
    except Exception as e:
        log_progress(f"Erro ao carregar dados: {e}")
        conn.close()
        raise
    return conn


def run_queries(conn: sqlite3.Connection, query_start: str = None, table_name: str = table_name):
    if query_start is None:
        query_start = f"SELECT * FROM {table_name};"
    return pd.read_sql(query_start, conn)


def log_progress(message: str):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now(timezone.utc)
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write((timestamp + ' - ' + message + '\n'))


log_progress("Iniciando processo ETL")

log_progress("Extra��o iniciada")
extracted_data = extract(base_url)
pd.set_option('display.max_rows', None, 'display.max_columns', None)
print(extracted_data)

log_progress("Extra��o finalizada")

log_progress("Transforma��o iniciada")
transformed_data = transform(extracted_data, exchange_rate)
# print(transformed_data)

log_progress("Fase de transforma��o finalizada")

log_progress(f"Carregando dados em {output_csv}")
load_to_csv(transformed_data, output_csv)

log_progress("Carregando dados em Banco de Dados")
connection_db = load_to_db(transformed_data)

log_progress("Carregamento finalizado")
log_progress("Processo ETL finalizado")

log_progress("Consultas SQL")

result = run_queries(connection_db, 'SELECT * FROM Largest_banks')
print(result)

result = run_queries(connection_db, 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks')
print(result)

result = run_queries(connection_db, 'SELECT Name FROM Largest_banks LIMIT 5')
print(result)
