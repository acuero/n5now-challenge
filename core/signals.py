"""
Script con "Django Signals" para ejecutar funcionalidades antes y despues de guardar un registro.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models.configuracion import Configuracion


@receiver(post_save, sender=Configuracion)
def crear_registro_unico_configuracion(sender, instance, created, **kwargs):
    """
    Señal que garantiza que el registro de Configuración sea único.
    Esta funcion no permitirá la existencia de dos o más registros para el modelo Configuracion.
    """
    if created and Configuracion.objects.count() > 1:
        instance.delete()
