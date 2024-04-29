"""
Script que contiene distintos validadores de datos para el proyecto.
"""
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.conf import settings
from core.models.configuracion import Configuracion
from core.models.vehiculo import Vehiculo
from core.models.persona import Persona
from rest_framework import status



def validate_fecha_infraccion(value):
    """
    Validador que verifica si una fecha de infracción es válida.
    Criterios:
        - No debe ser una fecha futura.
        - No debe superar la antigüedad configurada en core.Configuracion.dias_antiguedad_infraccion.
    """
    try:
        configuracion = Configuracion.objects.get(nombre=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY)
        fecha_infraccion = value.date()
        fecha_actual = datetime.now().date()
        fecha_ancla = fecha_actual - timedelta(configuracion.dias_antiguedad_infraccion)
        
        if not fecha_ancla <= fecha_infraccion <= fecha_actual:
            raise ValidationError(
                f"La fecha de infracción no puede ser futura ni superar {configuracion.dias_antiguedad_infraccion} días de antigüedad.",
                code=status.HTTP_400_BAD_REQUEST)
    except Configuracion.DoesNotExist:
        raise ValidationError(
            "No fué posible cargar configuración para validar fecha de infracción.",
            code=status.HTTP_404_NOT_FOUND)


def validate_placa_patente(value):
    """
    Validador que verifica existencia de vehiculo a partir de una placa patente.
    """
    try:
        Vehiculo.objects.get(placa_patente=value)
    except Vehiculo.DoesNotExist:
        raise ValidationError(
            "La placa patente provista no existe.",
            code=status.HTTP_404_NOT_FOUND)


def validate_email_propietario(value):
    """
    Validador que verifica la existencia de un propietario con el email provisto.
    """
    try:
        Persona.objects.get(email=value)
    except Persona.DoesNotExist:
        raise ValidationError(
            "El correo electrónico provisto no existe.",
            code=status.HTTP_404_NOT_FOUND)
