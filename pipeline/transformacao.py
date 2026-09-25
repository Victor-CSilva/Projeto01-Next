# %%
import pandas as pd
from pathlib import Path
pd.set_option("display.max.columns", None)


COLUNAS = [
  "NomTitularEmpreendimento", "NumCPFCNPJ", "NomMunicipio", "SigUF",
  "SigAgente", "DscPorte", "SigTipoGeracao", "MdaPotenciaInstaladaKW",
  "DscClasseConsumo", "CodSubGrupoTarifario", "DscSubGrupoTarifario"
]

# %%

def transformar() -> pd.DataFrame:
  BASE_DIR = Path(__file__).resolve().parent
  caminho_parquet = BASE_DIR.parent / "dados" / "brutos" / "empreendimento-geracao-distribuida.parquet"
  df = pd.read_parquet(caminho_parquet, columns=COLUNAS)
  df = df[df['DscPorte'] == 'Microgeracao']

  df = df.rename(columns={
    "NomTitularEmpreendimento": "titular",
    "NumCPFCNPJ": "cpf_cnpj",
    "NomMunicipio": "municipio",
    "SigUF": "uf",
    "SigAgente": "distribuidora",
    "DscPorte": "porte",
    "SigTipoGeracao": "fonte",
    "MdaPotenciaInstaladaKW": "potencia_kw",
    "DscClasseConsumo": "classe",
    "CodSubGrupoTarifario": "cod_subgrupo",
    "DscSubGrupoTarifario": "subgrupo"
    })
  
  df["potencia_kw"] = pd.to_numeric(
    df["potencia_kw"].astype(str).str.replace(",", "."), errors="coerce"
  )
  
  return df