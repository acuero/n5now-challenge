from django.db import models
from core.models.base import BaseModel
from core.validators import validate_fecha_infraccion


class Infraccion(BaseModel):
    """
    Modelo que representa una infraccion cargada a un vehiculo
    """
    vehiculo = models.ForeignKey(
        "core.Vehiculo",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Vehículo al que se le carga una infracción."
    )

    fecha_infraccion = models.DateTimeField(
        "Fecha de la infracción",
        blank=False,
        null=False,
        help_text="Fecha de la infracción",
        validators=[validate_fecha_infraccion]
    )

    oficial = models.ForeignKey(
        "core.Oficial",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Oficial que cargó la infracción."
    )

    class Meta:
        verbose_name = "Infracción"
        verbose_name_plural = "Infracciones"

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return f"Infracción #{self.pk}"
