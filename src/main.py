# synapsenet-vetra: Agente de IA Financiera
# Descripción: Este código define la base del agente IA usando Mistral para asesoramiento financiero.

from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

# Configuración del modelo Mistral (esto puede cambiar según la implementación real)
MISTRAL_API_URL = "https://api.mistral.ai/v1/agents/completions"
MISTRAL_API_KEY = os.getenv("uy2DxEZgA9z49oPJZ1hM7zJHvBOeFu9F", "")

# Endpoints de fuentes de datos financieros
ALPHA_VANTAGE_API = "https://www.alphavantage.co/query"
YAHOO_FINANCE_API = "https://query1.finance.yahoo.com/v7/finance/quote"
OPEN_EXCHANGE_RATES_API = "https://openexchangerates.org/api/latest.json"

if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY no está configurada")

@app.get("/consulta")
def consulta_ia(mensaje: str):
    """Endpoint para consultar a la IA financiera."""
    try:
        respuesta = requests.post(
            MISTRAL_API_URL,
            json={"prompt": mensaje},
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"}
        )
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta IA: {str(e)}")

@app.get("/datos")
def obtener_datos_financieros(ticker: str):
    """Obtiene datos financieros de Yahoo Finance."""
    try:
        url = f"{YAHOO_FINANCE_API}?symbols={ticker}"
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener datos financieros: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
