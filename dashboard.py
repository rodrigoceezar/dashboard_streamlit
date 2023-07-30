## Importando Bibliotecas
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

#Função de formatação de numero
def formata_num(valor, prefixo=''):
    for unidade in ['','mil']:
        if valor > 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'


##Adicionando um titulo
st.title('DASHBOARD DE VENDAS :shopping_trolley:')


url = 'https://labdados.com/produtos'
response = requests.get(url)

#Converter para JSON e Dataframe
dados = pd.DataFrame.from_dict(response.json())

coluna1, coluna2 = st.columns(2)

with coluna1:
    st.metric('Receita', formata_num(dados['Preço'].sum(), 'R$'))

with coluna2:
    st.metric('Quantidade de vendas', dados.shape[0])

st.dataframe(dados)