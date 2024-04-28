from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest.mock import patch, MagicMock
from datetime import datetime
from core.validators import validate_fecha_infraccion
from core.models.configuracion import Configuracion
from core.models.oficial import Oficial
from core.models.vehiculo import Vehiculo
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.core.management import call_command
from django.conf import settings


class TestN5Now(TestCase):
    """
    Subclase de pruebas para distintas funcionalidades del proyecto.
    
    docker compose run --rm -w /app django manage.py test
    """
    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        call_command("cargar_data_demo")


    @patch('core.validators.datetime')
    def test_fecha_infraccion_invalida_antigua(self, fecha_actual):
        """
        Test unitario que espera un "ValidationError" si la fecha de infracción 
        supera la antigüedad configurada en core.Configuracion.dias_antiguedad_infraccion. 
        
        Simulación:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-25.
            - La fecha de la infracción es: 2024-04-14
        """
        Configuracion.objects.filter(pk=1).update(dias_antiguedad_infraccion=10)
        fecha_actual.now.return_value.date.return_value = datetime(2024, 4, 25).date()
        fecha_infraccion = datetime(2024, 4, 14)
        with self.assertRaises(ValidationError):
            validate_fecha_infraccion(fecha_infraccion)


    @patch('core.validators.datetime')
    def test_fecha_infraccion_invalida_futura(self, fecha_actual):
        """
        Test unitario que espera un "ValidationError" si la fecha de infracción es futura. 
        
        Aplicamos un mock y simulamos que:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-25.
            - La fecha de la infracción es: 2024-04-26
        """
        Configuracion.objects.filter(pk=1).update(dias_antiguedad_infraccion=10)
        fecha_actual.now.return_value.date.return_value = datetime(2024, 4, 25).date()
        fecha_infraccion = datetime(2024, 4, 26)
        with self.assertRaises(ValidationError):
            validate_fecha_infraccion(fecha_infraccion)


    @patch('core.validators.datetime')
    def test_fecha_infraccion_valida(self, fecha_actual):
        """
        Test unitario que NO espera un "ValidationError" si la fecha de infracción es válida.
        Es decir, no es antigua ni futura. 
        
        Simulación:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-25.
            - La fecha de la infracción es: 2024-04-24
        """
        Configuracion.objects.filter(pk=1).update(dias_antiguedad_infraccion=10)
        fecha_actual.now.return_value.date.return_value = datetime(2024, 4, 25).date()
        fecha_infraccion = datetime(2024, 4, 24)
        try:
            validate_fecha_infraccion(fecha_infraccion)
        except ValidationError:
            self.fail("Test fallido para test_fecha_infraccion_valida.")


    def test_obtener_token_oficial(self):
        """
        Test unitario para probar la generación de tokens para los oficiales.
        """
        data = {"nui": "0007652", "password": "0007652"}
        response = self.client.post(reverse("obtener_token"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.json())


    def test_cargar_infraccion(self):
        """
        Test de integración para probar la carga de una infracción.
        """
        data_token = {"nui": "0007652", "password": "0007652"}
        response_token = self.client.post(reverse("obtener_token"), data_token, format='json')
        json_token = response_token.json()
        self.assertEqual(response_token.status_code, status.HTTP_200_OK)
        self.assertIn("token", json_token)

        data_infraccion = {
            "placa_patente": "A12345",
            "timestamp": "2024-04-01T10:15:00-0500",
            "comentarios": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        response = self.client.post(
            reverse("cargar_infraccion"), 
            data_infraccion, format='json', 
            HTTP_AUTHORIZATION=f"Bearer {json_token['token']}")
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("infraccion", json)
        self.assertIn("id", json['infraccion'])


    def test_cargar_infraccion_con_placa_invalida(self):
        """
        Test de integración para probar la carga de una infracción.
        Espera un HTTP_400_BAD_REQUEST si se provee una placa inválida (no existente).
        """
        data_token = {"nui": "0007652", "password": "0007652"}
        response_token = self.client.post(reverse("obtener_token"), data_token, format='json')
        json_token = response_token.json()
        self.assertEqual(response_token.status_code, status.HTTP_200_OK)
        self.assertIn("token", json_token)

        data_infraccion = {
            "placa_patente": "00000",
            "timestamp": "2024-04-01T10:15:00-0500",
            "comentarios": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        
        response = self.client.post(
            reverse("cargar_infraccion"), 
            data_infraccion, format='json', 
            HTTP_AUTHORIZATION=f"Bearer {json_token['token']}")
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("placa_patente", json)
        self.assertEqual(json['placa_patente'], ["La placa patente provista no existe."])


    @patch('core.validators.datetime')
    def test_cargar_infraccion_con_fecha_antigua(self, fecha_actual):
        """
        Test de integración para probar la carga de una infracción.
        Espera un HTTP_400_BAD_REQUEST si se provee una fecha inválida de acuerdo a la configuracion de antigüedad.
        
        Simulamos que:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-20
            - Fecha de la infraccion: 2024-04-09
        """
        Configuracion.objects.filter(pk=1).update(dias_antiguedad_infraccion=10)
        fecha_actual.now.return_value.date.return_value = datetime(2024, 4, 20).date()
        
        
        data_token = {"nui": "0007652", "password": "0007652"}
        response_token = self.client.post(reverse("obtener_token"), data_token, format='json')
        json_token = response_token.json()
        self.assertEqual(response_token.status_code, status.HTTP_200_OK)
        self.assertIn("token", json_token)

        data_infraccion = {
            "placa_patente": "A12345",
            "timestamp": "2024-01-09T10:15:00-0500",
            "comentarios": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        
        response = self.client.post(
            reverse("cargar_infraccion"), 
            data_infraccion, format='json', 
            HTTP_AUTHORIZATION=f"Bearer {json_token['token']}")
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("timestamp", json)
        
        configuracion = Configuracion.objects.get(nombre=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY)
        self.assertEqual(
            json['timestamp'], 
            [f"La fecha de infracción no puede ser futura ni superar {configuracion.dias_antiguedad_infraccion} días de antigüedad."])


    @patch('core.validators.datetime')
    def test_cargar_infraccion_con_fecha_futura(self, fecha_actual):
        """
        Test de integración para probar la carga de una infracción.
        Espera un HTTP_400_BAD_REQUEST si se provee una fecha futura.
        
        Simulamos que:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-20
            - Fecha de la infraccion: 2024-04-21
        """
        fecha_actual.now.return_value.date.return_value = datetime(2024, 4, 20).date()
        
        data_token = {"nui": "0007652", "password": "0007652"}
        response_token = self.client.post(reverse("obtener_token"), data_token, format='json')
        json_token = response_token.json()
        self.assertEqual(response_token.status_code, status.HTTP_200_OK)
        self.assertIn("token", json_token)

        data_infraccion = {
            "placa_patente": "A12345",
            "timestamp": "2023-04-21T10:15:00-0500",
            "comentarios": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        
        response = self.client.post(
            reverse("cargar_infraccion"), 
            data_infraccion, format='json', 
            HTTP_AUTHORIZATION=f"Bearer {json_token['token']}")
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("timestamp", json)
        
        configuracion = Configuracion.objects.get(nombre=settings.N5NOW_CHALLENGE_MAINCONFIG_KEY)
        self.assertEqual(
            json['timestamp'], 
            [f"La fecha de infracción no puede ser futura ni superar {configuracion.dias_antiguedad_infraccion} días de antigüedad."])
