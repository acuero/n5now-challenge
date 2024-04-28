"""
Script que contiene distintos validadores de datos para el proyecto.
"""
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.conf import settings
from core.models.configuracion import Configuracion
from core.models.vehiculo import Vehiculo



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
                f"La fecha de infracción no puede ser futura ni superar {configuracion.dias_antiguedad_infraccion} días de antigüedad.")
    except Configuracion.DoesNotExist:
        raise ValidationError("No fué posible cargar configuración para validar fecha de infracción.")


def validate_placa_patente(value):
    """
    Validador que verifica existencia de vehiculo a partir de una placa patente.
    """
    try:
        Vehiculo.objects.get(placa_patente=value)
    except Vehiculo.DoesNotExist:
        raise ValidationError("La placa patente provista no existe.")
