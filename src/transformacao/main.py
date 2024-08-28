import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.json', lines=True)

df['_source'] = "https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"
df['_data_coleta'] = datetime.now()