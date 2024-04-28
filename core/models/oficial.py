from django.db import models
from core.models.base import BaseModel
from django.contrib.auth.models import User

class Oficial(BaseModel):
    """
    Modelo que representa al oficial de policia.
    """
    nombre = models.CharField(
        "Nombre",
        blank=False,
        null=False,
        max_length=50,
        unique=True,
        help_text="Nombre del oficial."
    )

    nui = models.CharField(
        "Número único identificatorio",
        blank=False,
        null=False,
        max_length=10,
        unique=True,
        help_text="Número único identificatorio del oficial."
    )

    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Oficial"
        verbose_name_plural = "Oficiales"

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return f"{self.nombre} - {self.nui}"
