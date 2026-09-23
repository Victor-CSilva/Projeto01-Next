import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import altair as alt

load_dotenv()

usuario = os.getenv("DB_USUARIO")
senha = os.getenv("DB_SENHA")
host = os.getenv("DB_HOST")
porta = os.getenv("DB_PORTA")
banco = os.getenv("DB_BANCO")

engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

st.set_page_config(page_title="Radar de Fracionamento", layout="wide")
st.title("Radar de Fracionamento")
st.caption("Indícios para análise humana — não constitui acusação de fraude.")

query = """
SELECT
    "NomTitularEmpreendimento",
    "NomMunicipio",
    "NumCPFCNPJ",
    SUM("MdaPotenciaInstaladaKW") AS potencia_total,
    COUNT(*) AS qtd_empreendimentos
FROM empreendimentos_pe AS e
GROUP BY "NomTitularEmpreendimento", "NomMunicipio", "NumCPFCNPJ"
HAVING SUM("MdaPotenciaInstaladaKW") > 75
ORDER BY potencia_total DESC
"""

df_suspeitos = pd.read_sql(query, con=engine)

# --- Números-resumo ---
casos_por_cidade = (
    df_suspeitos.groupby("NomMunicipio")
    .size()
    .reset_index(name="casos_suspeitos")
    .sort_values("casos_suspeitos", ascending=False)
)


cidade_top = casos_por_cidade.iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Casos suspeitos", len(df_suspeitos))
col2.metric("kW sob suspeita", f'{df_suspeitos["potencia_total"].sum():,.0f}')
col3.metric("Cidade com mais casos", cidade_top["NomMunicipio"], f'{cidade_top["casos_suspeitos"]} casos')

# --- Gráfico: top 10 cidades ---
st.subheader("Top 10 cidades com mais casos suspeitos")
top10_cidades = casos_por_cidade.head(10)
grafico = (
    alt.Chart(top10_cidades)
    .mark_bar()
    .encode(
        x=alt.X("NomMunicipio", sort="-y", title="Município"),
        y=alt.Y("casos_suspeitos", title="Casos suspeitos"),
    )
)

st.altair_chart(grafico, use_container_width=True)

# --- Tabela por cidade, ranqueada dentro da cidade ---
st.subheader("Detalhamento por cidade")
cidades_disponiveis = casos_por_cidade["NomMunicipio"].tolist()
cidade_selecionada = st.selectbox("Selecione uma cidade", cidades_disponiveis)

df_cidade = (
    df_suspeitos[df_suspeitos["NomMunicipio"] == cidade_selecionada]
    .sort_values("potencia_total", ascending=False)
)

st.dataframe(df_cidade, use_container_width=True)