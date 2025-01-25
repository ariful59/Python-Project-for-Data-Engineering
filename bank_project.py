import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attr = ["Name", "MC_USD_Billion"]
table_attr_final = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
db_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"
csv_path  = "./Largest_banks_data.csv"

def log_progress(msg):
    timestamp = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp)
    with open (f'./{log_file}', 'a') as f:
        f.write(timestamp+" : "+ msg + '\n')

def extract(url, table_attr):
    df = pd.DataFrame(columns=table_attr)
    html = requests.get(url).text
    data = BeautifulSoup(html, 'html.parser')
    table = data.find_all('tbody')
    rows = table[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[1].find('a'):
                data = {
                    table_attr[0] : col[1].text.strip(),
                    table_attr[1] : float(col[2].contents[0].strip())
                }
                df1 = pd.DataFrame(data, index=[0])
                df = pd.concat([df,df1], ignore_index = True)
    return df

def transform(df, path):
    data = pd.read_csv(path)
    data = data.set_index('Currency').to_dict()['Rate']

    for k, f in zip(data.keys(), data.values()):
        exchange = float(f)
        df[f'MC_{k}_Billion'] = [np.round(x * exchange, 2) for x in df['MC_USD_Billion']]
    print(df)
    return df

def load_to_csv(df, output):
    df.to_csv(output)

def load_to_db(df, sql_conn, table):
    df.to_sql(table, sql_conn, if_exists='replace', index=False)

def run_query(query_state, sql_conn):
    query_state =pd.read_sql_query(query_state, sql_conn)
    return query_state

log_progress("Declaring known values")
log_progress("Preliminaries complete. Initiating ETL process")
data = extract(url, table_attr)
log_progress("Data extraction complete. Initiating Transformation process")
data = transform(data, path="exchange_rate.csv")

print(data['MC_EUR_Billion'][4])
log_progress("Data transformation complete. Initiating Loading process")
load_to_csv(data, csv_path)
log_progress("Data saved to CSV file")
log_progress("Initiate SQLite3 connection")
log_progress("SQL Connection initiated")
sq = sqlite3.connect(db_name)
load_to_db(data, sq, table_name)
log_progress("Data loaded to Database as a table, Executing queries")
query_statement1 = f"SELECT * FROM {table_name}"
query_statement2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
query_statement3 = f"SELECT NAME FROM {table_name} LIMIT 5"
print(run_query(query_statement1, sq))
print(run_query(query_statement2, sq))
print(run_query(query_statement3, sq))
log_progress("Process Complete")
sq.close()
log_progress("Close SQLite3 connection")
log_progress("Server Connection closed")

