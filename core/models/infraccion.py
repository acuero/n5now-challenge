from django.db import models
from core.models.base import BaseModel
from core.models.vehiculo import Vehiculo
from core.models.oficial import Oficial


class Infraccion(BaseModel):
    """
    Modelo que representa una infraccion cargada a un vehiculo
    """
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Vehículo al que se le carga una infracción."
    )

    fecha_infraccion = models.DateTimeField(
        "Fecha de la infracción",
        blank=False,
        null=False,
        help_text="Fecha de la infracción"
    )

    oficial = models.ForeignKey(
        Oficial,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Oficial que cargó la infracción."
    )

    class Meta:
        verbose_name = "Infracción"
        verbose_name_plural = "Infracciones"
