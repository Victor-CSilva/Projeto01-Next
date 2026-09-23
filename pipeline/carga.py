from sqlalchemy import create_engine
from transformacao import transformar
import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("DB_USUARIO")
senha = os.getenv("DB_SENHA")
host = os.getenv("DB_HOST")
porta = os.getenv("DB_PORTA")
banco = os.getenv("DB_BANCO")

engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

df = transformar()

df.to_sql("empreendimentos_pe", con=engine, if_exists="replace", index=False)
