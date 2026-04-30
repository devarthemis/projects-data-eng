import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime, timezone

# Extração
base_url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

data_json = 'Countries_by_GDP.json'
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
attribute_list = ['Country', 'GDP_USD_billion']

data_list = []

log_file = 'etl_project_log.txt'

def extract(base_url:str):
    soup = BeautifulSoup(requests.get(base_url).text, 'lxml')

    table = soup.find_all('tbody')[2]
    rows_countries = table.find_all('tr')[3::]

    for row in rows_countries:
        cols = row.find_all('td')
        if len(cols) != 0:
            gdp_raw = cols[2].text.strip().replace(',', '')
            data_dict = {
                "Country": cols[0].text.strip(),
                "GDP_USD_billion": round(float(gdp_raw) / 1000, 2) if gdp_raw.replace('.', '').isdigit() else None
            }
            data_list.append(data_dict)
    return data_list

def trasform_to_json(df:pd.DataFrame, data_json:str):
    return df.to_json(data_json, orient='records')

def load_db(db_name:str, table_name:str, df:pd.DataFrame):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    return conn

def log_progress(message:str):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now(timezone.utc)
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write((timestamp + ' - ' + message + '\n'))

# Testando
log_progress("Iniciando processo ETL")
log_progress("Extração iniciada")
extract_data = extract(base_url)
df = pd.DataFrame(extract_data, columns=attribute_list)
log_progress(f"Extração finalizada. {len(extract_data)} países encontrados.")
log_progress("Salvando JSON em Countries_by_GDP.json")
trasform_to_json(df, data_json)
log_progress("JSON salvo com sucesso.")
log_progress("Salvando dados em World_Economies.db")
connection_db = load_db(db_name, table_name, df)
log_progress("Banco de dados salvos com sucesso.")

query_startment = f"SELECT * FROM {table_name} WHERE GDP_USD_billion > 100"
query_output = pd.read_sql(query_startment, connection_db)
print(query_output)

connection_db.close()