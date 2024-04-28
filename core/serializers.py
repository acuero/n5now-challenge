"""
Serializadores para presentacion de datos.
"""
from rest_framework import serializers
from core.validators import validate_fecha_infraccion, validate_placa_patente
from core.models.infraccion import Infraccion


class OficialObtainTokenSerializer(serializers.Serializer):
    """
    Serializador con la definición de la autenticación de Oficiales.
    """
    nui = serializers.CharField(max_length=10, trim_whitespace=True)
    password = serializers.CharField(style={'input_type': 'password'})


class CargarInfraccionSerializer(serializers.Serializer):
    """
    Serializador con la definición de la data con la que se cargará la infracción.
    """
    placa_patente = serializers.CharField(
        required=True,
        max_length=10, 
        trim_whitespace=True, 
        validators=[validate_placa_patente])
    
    timestamp = serializers.DateTimeField(
        required=True,
        validators=[validate_fecha_infraccion])
    
    comentarios = serializers.CharField(
        required=True,
        style={'base_template': 'textarea.html'})


class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        depth = 1
        fields = ['id', 'vehiculo', 'fecha_infraccion', 'oficial', 'fecha_creacion', 'ultima_modificacion']
        read_only_fields = ['vehiculo', 'fecha_infraccion', 'oficial']
