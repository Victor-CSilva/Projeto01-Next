# %%
import pandas as pd
from pathlib import Path
pd.set_option("display.max.columns", None)

# %%

def transformar() -> pd.DataFrame:
  BASE_DIR = Path(__file__).resolve().parent
  caminho_parquet = BASE_DIR.parent / "dados" / "brutos" / "empreendimento-geracao-distribuida.parquet"
  df = pd.read_parquet(caminho_parquet)
  df = df[df['DscPorte'] == 'Microgeracao']
  df = df[df['SigAgente'] == 'Neoenergia PE']
  df = df[df['SigUF'] == 'PE']
  df = df[df['SigTipoGeracao'] == 'UFV']
  return df
