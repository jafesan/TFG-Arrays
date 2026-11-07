import os
import requests

IFTTT_URL = os.environ.get("IFTTT_URL")
URL_PARADA_ABENARABI = "https://tranviademurcia.es/linea/paradas/abenarabi/"

def comprobar_tranvia():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }
        response = requests.get(URL_PARADA_ABENARABI, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Simulación o lectura de los minutos reales
            minutos_restantes = 4 
            print(f"Minutos restantes: {minutos_restantes}")
            
            if minutos_restantes <= 5 and IFTTT_URL:
                requests.get(IFTTT_URL)
                print("¡Alerta enviada a IFTTT!")
        else:
            print("Error al conectar con la web:", response.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    comprobar_tranvia()
