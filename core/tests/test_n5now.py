from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest.mock import patch, MagicMock
from datetime import datetime
from core.validators import validate_fecha_infraccion
from core.models.configuracion import Configuracion
from core.models.oficial import Oficial
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse



class TestN5Now(TestCase):
    """
    Subclase de pruebas para distintas funcionalidades del proyecto.
    
    docker compose run --rm -w /app django manage.py test
    """
    def setUp(self):
        self.client = APIClient()
    
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
        oficial = Oficial.objects.create(nombre="WADE WILSON", nui="998877")
        data = {"nui": oficial.nui, "password": oficial.nui}
        response = self.client.post(reverse("obtener_token"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.json())
    
    def test_obtener_token_oficial_y_cargar_infraccion(self):
        """
        Test de integración para probar la carga de una infracción.
        """
        oficial = Oficial.objects.create(nombre="PETER PARKER", nui="112233")
        data_token = {"nui": oficial.nui, "password": oficial.nui}
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
