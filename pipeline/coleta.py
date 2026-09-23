import requests
from pathlib import Path

def baixar_arquivo(url: str, pasta_destino: Path) -> Path:
    pasta_destino.mkdir(parents=True, exist_ok=True)
    nome_arquivo = url.split("/")[-1]  # pega o nome do arquivo a partir da URL
    caminho_arquivo = pasta_destino / nome_arquivo

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(caminho_arquivo, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Arquivo salvo em: {caminho_arquivo.resolve()}")
    return caminho_arquivo


urls = [
    "https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/cd29f6eb-e08d-4db7-b6fb-ed6e3b682d27/download/empreendimento-geracao-distribuida.parquet",
    "https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/703c4cb8-b7e2-4f27-a9bb-7e55324a88a4/download/empreendimento-gd-informacoes-tecnicas-fotovoltaica.parquet",
]

pasta_destino = Path("../dados/brutos")

for url in urls:
    baixar_arquivo(url, pasta_destino)