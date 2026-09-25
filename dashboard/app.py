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
    titular,
    municipio,
    cpf_cnpj,
    fonte,
    classe,
    subgrupo,
    SUM(potencia_kw) AS potencia_total,
    COUNT(*) AS qtd_empreendimentos
FROM empreendimentos_pe AS e
WHERE distribuidora = 'Neoenergia PE' AND uf = 'PE'
GROUP BY titular, municipio, cpf_cnpj, fonte, classe, subgrupo
HAVING SUM(potencia_kw) > 75
ORDER BY potencia_total DESC
"""

df_suspeitos = pd.read_sql(query, con=engine)

query_cep = """
SELECT
    cpf_cnpj,
    cep,
    COUNT(*) AS qtd_usinas_no_cep
FROM empreendimentos_pe
WHERE distribuidora = 'Neoenergia PE' AND uf = 'PE'
GROUP BY cpf_cnpj, cep
HAVING COUNT(*) > 1
"""
df_cep_repetido = pd.read_sql(query_cep, con=engine)

df_suspeitos["fator_alarmante_cep"] = df_suspeitos["cpf_cnpj"].isin(df_cep_repetido["cpf_cnpj"])

df_suspeitos["excedente_kw"] = df_suspeitos["potencia_total"] - 75

# --- Montagem do ranking ---
df_suspeitos["score"] = (
    0.5 * df_suspeitos["excedente_kw"].rank(pct=True) +
    0.3 * df_suspeitos["qtd_empreendimentos"].rank(pct=True) +
    0.2 * df_suspeitos["fator_alarmante_cep"].astype(int)
)

df_suspeitos = df_suspeitos.sort_values("score", ascending=False)

# --- Números-resumo ---
casos_por_cidade = (
    df_suspeitos.groupby("municipio")
    .size()
    .reset_index(name="casos_suspeitos")
    .sort_values("casos_suspeitos", ascending=False)
)


cidade_top = casos_por_cidade.iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Casos suspeitos", len(df_suspeitos))
col2.metric("kW sob suspeita", f'{df_suspeitos["potencia_total"].sum():,.0f}')
col3.metric("Cidade com mais casos", cidade_top["municipio"], f'{cidade_top["casos_suspeitos"]} casos')

# --- Gráfico: top 10 cidades ---
st.subheader("Top 10 cidades com mais casos suspeitos")
top10_cidades = casos_por_cidade.head(10)
grafico = (
    alt.Chart(top10_cidades)
    .mark_bar()
    .encode(
        x=alt.X("municipio", sort="-y", title="Município"),
        y=alt.Y("casos_suspeitos", title="Casos suspeitos"),
    )
)

st.altair_chart(grafico, use_container_width=True)

# --- Tabela por cidade, ranqueada dentro da cidade ---
st.subheader("Detalhamento por cidade")
cidades_disponiveis = casos_por_cidade["municipio"].tolist()
cidade_selecionada = st.selectbox("Selecione uma cidade", cidades_disponiveis)

df_cidade = (
    df_suspeitos[df_suspeitos["municipio"] == cidade_selecionada]
    .sort_values("potencia_total", ascending=False)
)

st.dataframe(df_cidade, use_container_width=True)

st.header("Perfil dos casos suspeitos em PE")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("Por fonte")
    por_fonte = df_suspeitos["fonte"].value_counts().reset_index()
    por_fonte.columns = ["fonte", "casos"]
    grafico_fonte = (
        alt.Chart(por_fonte)
        .mark_bar()
        .encode(x=alt.X("fonte", sort="-y"), y="casos")
    )
    st.altair_chart(grafico_fonte, use_container_width=True)

with col_b:
    st.subheader("Por classe")
    por_classe = df_suspeitos["classe"].value_counts().reset_index()
    por_classe.columns = ["classe", "casos"]
    grafico_classe = (
        alt.Chart(por_classe)
        .mark_bar()
        .encode(x=alt.X("classe", sort="-y"), y="casos")
    )
    st.altair_chart(grafico_classe, use_container_width=True)

with col_c:
    st.subheader("Por subgrupo")
    por_subgrupo = df_suspeitos["subgrupo"].value_counts().reset_index()
    por_subgrupo.columns = ["subgrupo", "casos"]
    grafico_subgrupo = (
        alt.Chart(por_subgrupo)
        .mark_bar()
        .encode(x=alt.X("subgrupo", sort="-y"), y="casos")
    )
    st.altair_chart(grafico_subgrupo, use_container_width=True)


st.header("Pernambuco em comparação com outros estados")

query_nacional = """
SELECT
    uf,
    titular,
    municipio,
    cpf_cnpj,
    fonte,
    SUM(potencia_kw) AS potencia_total,
    COUNT(*) AS qtd_empreendimentos
FROM empreendimentos_pe
GROUP BY uf, titular, municipio, cpf_cnpj, fonte
HAVING SUM(potencia_kw) > 75
"""

df_nacional = pd.read_sql(query_nacional, con=engine)


resumo_por_uf = (
    df_nacional.groupby("uf")
    .agg(casos_suspeitos=("uf", "size"), kw_suspeito=("potencia_total", "sum"))
    .reset_index()
    .sort_values("casos_suspeitos", ascending=False)
)


grafico_uf = (
    alt.Chart(resumo_por_uf.head(15))
    .mark_bar()
    .encode(
        x=alt.X("uf", sort="-y", title="Estado"),
        y=alt.Y("casos_suspeitos", title="Casos suspeitos"),
        color=alt.condition(
            alt.datum.uf == "PE", alt.value("orange"), alt.value("steelblue")
        ),
    )
)

st.altair_chart(grafico_uf, use_container_width=True)