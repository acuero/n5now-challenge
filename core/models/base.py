from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Modelo que actua como clase abstracta que cada modelo heredará en el proyecto.
    Esta clase le proveerá a cada modelo los siguientes atributos:
        - fecha_creacion (DateTimeField)
        - ultima_modificacion (DateTimeField)
        - observaciones (CharField)
    """
    fecha_creacion = models.DateTimeField(
        "Fecha de creación",
        auto_now_add=True,
        help_text="Marca de tiempo de la creación de un objeto.")

    ultima_modificacion = models.DateTimeField(
        "Ultima modificación",
        auto_now=True,
        help_text="Marca de tiempo de la última modificación de un objeto.")

    observaciones = models.TextField(
        "Observaciones",
        blank=True,
        max_length=255,
        help_text="Campo abierto para añadir alguna descripción u observación."
    )

    class Meta:
        abstract = True
        get_latest_by = 'fecha_creacion'
        ordering = ['fecha_creacion',]
