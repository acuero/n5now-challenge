from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    """
    Comando que carga datos de demostración de los distintos modelos del proyecto.
    Este comando será llamado desde el entrypoint de docker cuando se construya la imágen del proyecto.
    """
    help = "Carga datos de demostración para los modelos del proyecto usando fixtures."

    def handle(self, *args, **options):
        """
        Implementación del comando.
        """
        # El orden en que se deben aplicar los fixtures es importante
        fixtures = [
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "configuracion.json",
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "personas.json",
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "marcas.json",
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "vehiculos.json",
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "oficiales.json",
            settings.N5NOW_CHALLENGE_FIXTURES_PATH + "infracciones.json"
        ]

        # Aplicamos uno a uno cada fixture
        for fixture in fixtures:
            self.stdout.write(f"Cargando fixture '{fixture}'")
            call_command("loaddata", fixture)
        self.stdout.write(self.style.SUCCESS('Datos de demostración cargados correctamente.'))
