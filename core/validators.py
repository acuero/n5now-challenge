"""
Script que contiene distintos validadores de datos para el proyecto.
"""
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.conf import settings
from core.models.configuracion import Configuracion



def validate_fecha_infraccion(value):
    """
    Validador que verifica si una fecha de infracción es válida.
    Criterios:
        - No debe ser una fecha futura.
        - No debe superar la antigüedad configurada en core.Configuracion.dias_antiguedad_infraccion.
    """
    try:
        configuracion = Configuracion.objects.filter(nombre=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY).first()
        fecha_actual = datetime.now().date()
        fecha_ancla = fecha_actual - timedelta(configuracion.dias_antiguedad_infraccion)
        if not fecha_ancla <= value <= fecha_actual:
            raise ValidationError(
                f"la fecha de infracción no puede ser futura ni superar {configuracion.dias_antiguedad_infraccion} días de antigüedad.")
    except Configuracion.DoesNotExist:
        raise ValidationError("No fué posible cargar configuración para validar fecha de infracción.")
