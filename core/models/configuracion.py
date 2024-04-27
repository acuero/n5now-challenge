from django.db import models
from core.models.base import BaseModel
from django.conf import settings
from django.core.exceptions import ValidationError


class Configuracion(BaseModel):
    """
    Modelo que representa la configuracion general para la correcta ejecucion de la logica del negocio
    """
    nombre = models.CharField(
        "Configuración",
        max_length=90,
        null=False,
        blank=False,
        default=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY,
        unique=True,
        help_text="Configuración General."
    )

    dias_antiguedad_infraccion = models.PositiveIntegerField(
        "Antiguedad válida de una infraccion (dias)",
        default=90,
        unique=True,
        help_text="Una infracción se considera válida si su antiguedad en días es menor o igual a este valor."
    )

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuración"

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return self.nombre

    def save(self, *args, **kwargs):
        """
        Sobreescribimos metodo nativo "save" para garantizar que este modelo tenga un único registro.
        """
        try:
            configuracion_existente = Configuracion.objects.get()
            raise ValidationError("No es posible agregar un nuevo registro de Configuración.")
        except Configuracion.DoesNotExist:
            super().save(*args, **kwargs)
