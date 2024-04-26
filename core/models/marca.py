from django.db import models
from core.models.base import BaseModel


class Marca(BaseModel):
    """
    Modelo que representa la marca de un vehiculo.
    """
    nombre = models.CharField(
        "Nombre",
        blank=False,
        null=False,
        max_length=30,
        unique=True,
        help_text="Nombre de la marca."
    )

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return self.nombre
