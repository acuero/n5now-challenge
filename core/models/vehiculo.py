from django.db import models
from core.models.base import BaseModel
from core.models.marca import Marca
from core.models.persona import Persona
from colorfield.fields import ColorField


class Vehiculo(BaseModel):
    """
    Modelo que representa el vehiculo al que se le cargaran infracciones.
    """
    placa_patente = models.CharField(
        "Placa patente",
        max_length=10,
        blank=False,
        null=False,
        unique=True,
        help_text="Placa de patente del vehículo."
    )

    marca = models.ForeignKey(
        Marca,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='vehiculos',
        help_text="Marca del vehículo."
    )

    color = ColorField(
        "Color",
        default="#FF0000",
        help_text="Color del vehículo."
    )

    propietario = models.ForeignKey(
        Persona,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='vehiculos',
        help_text="Propietario del vehículo."
    )

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return f"{self.placa_patente} - {self.marca.nombre}"

