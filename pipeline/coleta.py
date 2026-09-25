import requests
from pathlib import Path

url = "https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/cd29f6eb-e08d-4db7-b6fb-ed6e3b682d27/download/empreendimento-geracao-distribuida.parquet"

pasta_destino = Path("../dados/brutos")
pasta_destino.mkdir(parents=True, exist_ok=True)

caminho_arquivo = pasta_destino / "empreendimento-geracao-distribuida.parquet"

response = requests.get(url, stream=True)
response.raise_for_status()

with open(caminho_arquivo, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

print(f"Arquivo salvo em: {caminho_arquivo.resolve()}")