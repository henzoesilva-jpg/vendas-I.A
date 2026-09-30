# Author: Raphael Campos Squilaro
# Project: Automatization of sales

# -------- LIBRARIES --------
import streamlit as st # pip install streamlit
import pandas as pd # pip install pandas
import json
from google import genai # pip install google-genai

# -------- CONFIGURATIONS ---------
with open("token.json", "r") as arquivo:
    dados = json.load(arquivo)

# Create a client for Google
client = genai.Client(api_key=dados["api_key"])

# -------- INTERFACE --------

# Set title of the page
st.title("🤖 AGENTES DE IA - VENDAS")

# open a spreadsheet
arquivo = st.file_uploader(
    "Escolha a planilha",
    type=["xlsx"]
)

# condicional for reading data of spreadsheet
if arquivo:
    dados = pd.read_excel(arquivo)
    st.subheader("Dados da planilha")
    st.dataframe(dados)
    pergunta = st.text_input("O que deseja saber?")