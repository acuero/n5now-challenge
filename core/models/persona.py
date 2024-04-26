from django.db import models
from core.models.base import BaseModel


class Persona(BaseModel):
    """
    Modelo que representa una persona propietaria de algun vehiculo.
    """
    nombre = models.CharField(
        "Nombre",
        blank=False,
        null=False,
        max_length=50,
        help_text="Nombre del propietario."
    )

    email = models.EmailField(
        "Correo electrónico",
        unique=True,
        help_text="Correo electrónico del propietario."
    )

    def __str__(self) -> str:
        """Representacion de la instancia como cadena de caracteres."""
        return self.nombre
