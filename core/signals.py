"""
Script con señales (Signals) que disparan alguna funcionalidad 
antes o después de un evento determinado.
"""
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from core.models.configuracion import Configuracion
from core.models.oficial import Oficial
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


@receiver(post_migrate)
def precargar_configuracion_general(sender, **kwargs):
    """
    Signal para crear registro único de configuración.
    """
    if sender.name == 'core':
        if Configuracion.objects.exists():
            return
        Configuracion.objects.create(
            nombre=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY, 
            dias_antiguedad_infraccion=90)


@receiver(post_save, sender=Oficial)
def crear_usuario_oficial(sender, instance, created, **kwargs):
    """
    Signal para crear usuario asociado al oficial.
    """
    if created:
        User = get_user_model()
        usuario = User.objects.create_user(username=instance.nui, password=instance.nui)
        Oficial.objects.filter(pk=instance.pk).update(usuario=usuario)
