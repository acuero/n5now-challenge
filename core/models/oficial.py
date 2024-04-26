from django.db import models
from core.models.base import BaseModel
from django.contrib.auth.models import AbstractUser, Group, Permission


class Oficial(BaseModel, AbstractUser):
    """
    Modelo que representa al oficial de policia.
    Hereda de AbstractUser para otorgarle la funcionalidad de autenticacion nativa de usuarios.
    """
    USERNAME_FIELD = 'nui'
    REQUIRED_FIELDS = ['nombre']

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

    """
    groups: Campo adicional fuera de la logica del negocio para solucionar error que se presenta al heredar AbstractUser:
        auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 
        'auth.User.groups' clashes with reverse accessor for 'core.Oficial.groups'.
    """
    groups = models.ManyToManyField(
        Group,
        related_name='oficiales_groups'
    )

    """
    user_permissions: Campo adicional fuera de la logica del negocio para solucionar error que se presenta al heredar AbstractUser:
        auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 
        'auth.User.user_permissions' clashes with reverse accessor for 'core.Oficial.user_permissions'.
    """
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='oficial_user_permissions'
    )

    class Meta:
        verbose_name = "Oficial"
        verbose_name_plural = "Oficiales"

    def __str__(self):
        """Representacion de la instancia como cadena de caracteres."""
        return f"{self.nombre} - {self.nui}"
