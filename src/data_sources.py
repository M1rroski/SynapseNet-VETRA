import requests
from src.config import ALPHA_VANTAGE_API, YAHOO_FINANCE_API, OPEN_EXCHANGE_RATES_API

def obtener_datos_yahoo(ticker: str):
    """Obtiene datos de Yahoo Finance para un ticker."""
    url = f"{YAHOO_FINANCE_API}?symbols={ticker}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al obtener datos de Yahoo Finance: {str(e)}")

def obtener_datos_alpha_vantage(ticker: str):
    """Obtiene datos de Alpha Vantage para un ticker."""
    url = f"{ALPHA_VANTAGE_API}?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=TU_API_KEY"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al obtener datos de Alpha Vantage: {str(e)}")

def obtener_datos_open_exchange():
    """Obtiene los datos de tasas de cambio de Open Exchange Rates."""
    try:
        respuesta = requests.get(OPEN_EXCHANGE_RATES_API)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al obtener datos de Open Exchange Rates: {str(e)}")
