import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('../data/quoes.db')

df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

conn.close()

st.title('Pesquisa de Mercado - Tênis esportivo no Mercado Livre')
st.subheader('KPIs Principais do sistemas')
col1, col2, col3, = st.columns(3)

total_itens = df.shape[0] 
col1.metric(label="Número Total de Itens", value=total_itens)