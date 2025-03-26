import requests
from src.config import MISTRAL_API_URL, MISTRAL_API_KEY

def consultar_mistral(mensaje: str):
    """Consulta a la IA de Mistral con un mensaje."""
    try:
        respuesta = requests.post(
            MISTRAL_API_URL,
            json={"prompt": mensaje, "model": "mistral-7b"},
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"}
        )
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la consulta IA: {str(e)}"}
