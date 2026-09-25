import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_BRUTOS = BASE_DIR / "dados" / "brutos"

url = "https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/cd29f6eb-e08d-4db7-b6fb-ed6e3b682d27/download/empreendimento-geracao-distribuida.parquet"

def baixar_arquivo(url: str, pasta: Path) -> Path:
    pasta.mkdir(parents=True, exist_ok=True)
    caminho_arquivo = PASTA_BRUTOS / "empreendimento-geracao-distribuida.parquet"
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(caminho_arquivo, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Arquivo salvo em: {caminho_arquivo.resolve()}")
    return caminho_arquivo

if __name__ == "__main__":
    baixar_arquivo(url, PASTA_BRUTOS)
