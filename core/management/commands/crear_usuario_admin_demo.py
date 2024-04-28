from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    """
    Comando que crea un usuario administrador para demostración.
    Este comando será llamado desde el entrypoint de docker cuando se construya la imágen del proyecto.
    """
    help = "Crea un usuario administrador para demostración."

    def handle(self, *args, **options):
        """
        Implementación del comando.
        """
        User = get_user_model()
        if not User.objects.filter(email=settings.N5NOW_CHALLENGE_USER_EMAIL_DEMO).exists():
            User.objects.create_superuser(
                username=settings.N5NOW_CHALLENGE_USERNAME_DEMO,
                password=settings.N5NOW_CHALLENGE_USER_PASSWORD_DEMO,
                email=settings.N5NOW_CHALLENGE_USER_EMAIL_DEMO
            )
            self.stdout.write(self.style.SUCCESS('Se ha creado un usuario administrador de demostración.'))
            self.stdout.write(f"** Credenciales **")
            self.stdout.write(f"Nombre de usuario: {settings.N5NOW_CHALLENGE_USERNAME_DEMO}")
            self.stdout.write(f"Contraseña: {settings.N5NOW_CHALLENGE_USER_PASSWORD_DEMO}")
            self.stdout.write(f"E-mail: {settings.N5NOW_CHALLENGE_USER_EMAIL_DEMO}")
        else:
            self.stdout.write(self.style.NOTICE('Ya existe un usuario administrador de demostración.'))
