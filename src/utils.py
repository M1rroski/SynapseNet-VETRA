def formatear_respuesta(respuesta):
    """Formatea la respuesta del modelo Mistral."""
    return {"mensaje": respuesta.get("text", "No se obtuvo respuesta")}
