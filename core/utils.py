"""
Script para personalizar las excepciones que se presenten en el consumo de las apis.
"""
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Método que añade el codigo HTTP de la excepción.
    """
    response = exception_handler(exc, context)
    code = response.status_code
    exc_codes = list(exc.get_codes().values())
    
    if exc_codes and len(exc_codes) > 0 and len(exc_codes[0]) > 0:
        code = exc_codes[0][0]
        
    if response is not None:
        response.data['status_code'] = code

    return response
