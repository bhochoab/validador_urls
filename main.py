import requests
import pandas as pd

def verificar_urls(archivo_entrada: str, archivo_salida: str):
    resultados = []
    with open(archivo_entrada, "r") as f:
        urls = f.read().splitlines()

    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            resultados.append({"url": url, "status": r.status_code})
        except requests.exceptions.RequestException as e:
            resultados.append({"url": url, "status": str(e)})

    df = pd.DataFrame(resultados)
    df.to_csv(archivo_salida, index=False)
    print(f"Resultados guardados en {archivo_salida}")

if __name__ == "__main__":
    verificar_urls("urls.txt", "resultados.csv")
