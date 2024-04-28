"""
Serializadores para presentacion de datos.
"""
from rest_framework import serializers


class OficialObtainTokenSerializer(serializers.Serializer):
    """
    Serializador con la definición de la autenticación de Oficiales.
    """
    nui = serializers.CharField()
    password = serializers.CharField()


class CargarInfraccionSerializer(serializers.Serializer):
    """
    Serializador con la definición de la data con la que se cargará la infracción.
    """
    placa_patente = serializers.CharField()
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField()
