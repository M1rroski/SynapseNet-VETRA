import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde un archivo .env

MISTRAL_API_URL = "https://api.mistral.ai/v1/agents/untitled-agent-0f687954/completions"
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

ALPHA_VANTAGE_API = "https://www.alphavantage.co/query"
YAHOO_FINANCE_API = "https://query1.finance.yahoo.com/v7/finance/quote"
OPEN_EXCHANGE_RATES_API = "https://openexchangerates.org/api/latest.json"

if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY no está configurada correctamente")
