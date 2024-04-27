from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest import mock
from datetime import datetime
from core.validators import validate_fecha_infraccion



class N5NowTests(TestCase):
    """
    Subclase de pruebas para distintas funcionalidades del proyecto.
    """
    
    def test_fecha_infraccion_invalida_antigua(self):
        """
        Test que espera un "ValidationError" si la fecha supera la antigüedad 
        configurada en core.Configuracion.dias_antiguedad_infraccion. 
        
        Aplicamos un mock y simulamos que:
            - Antigüedad de infracciones permitida en dias: 10 días.
            - La fecha actual es: 2024-04-25.
            - La fecha de la infracción es: 2024-04-14
            
        """
        with self.assertRaises(ValidationError):
            ruta_mock_configuracion = "core.validators.validate_fecha_infraccion.configuracion"
            ruta_mock_fecha_actual = "core.validators.validate_fecha_infraccion.fecha_actual"
            mock_configuracion = mock.Mock()
            mock_fecha_actual = mock.Mock()
            
            with mock.patch(ruta_mock_configuracion, mock_configuracion) as mock_conf_con,\
                mock.patch(ruta_mock_fecha_actual, mock_fecha_actual) as mock_fecha_actual_con:
                    mock_conf_con.return_value.__setattr__("dias_antiguedad_infraccion", 10)
                    mock_fecha_actual_con.return_value = datetime(2024, 4, 25)
                    validate_fecha_infraccion(datetime(2024, 4, 14))

    def test_fecha_infraccion_invalida_futura(self):
        pass
    
    def test_fecha_infraccion_valida(self):
        pass

