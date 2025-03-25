from fastapi import APIRouter, HTTPException
from mistral_model import consultar_mistral
from data_sources import obtener_datos_yahoo
from utils import formatear_respuesta

router = APIRouter()

@router.get("/consulta")
def consulta_ia(mensaje: str):
    """Endpoint para consultar a la IA financiera de Mistral."""
    respuesta = consultar_mistral(mensaje)
    return formatear_respuesta(respuesta)

@router.get("/datos")
def obtener_datos_financieros(ticker: str):
    """Endpoint para obtener datos financieros de Yahoo Finance."""
    respuesta = obtener_datos_yahoo(ticker)
    return formatear_respuesta(respuesta)
