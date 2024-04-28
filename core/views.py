"""
Vistas (endpoints) del api.
"""
from rest_framework import views, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from core.serializers import OficialObtainTokenSerializer, CargarInfraccionSerializer, InfraccionSerializer
from core.management.authentication import JWTOficialAuth
from core.models.oficial import Oficial
from core.models.infraccion import Infraccion
from core.models.vehiculo import Vehiculo
from django.contrib.auth import authenticate
from core.permissions import OficialIsAuthenticated


class ObtenerTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OficialObtainTokenSerializer
    authentication_classes = [JWTOficialAuth]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        nui = serializer.validated_data.get('nui')
        password = serializer.validated_data.get('password')
        
        oficial = Oficial.objects.filter(nui=nui).first()
        if oficial is None:
            return Response({'message': 'Oficial no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        usuario_oficial = authenticate(username=nui, password=password)
        if not usuario_oficial:
            return Response({'message': 'Credenciales inválidas.'}, status=status.HTTP_400_BAD_REQUEST)

        jwt_token = JWTOficialAuth.crear_jwt(oficial)
        return Response({'token': jwt_token}, status=status.HTTP_200_OK)



class CargarInfraccionView(views.APIView):
    permission_classes = [OficialIsAuthenticated]
    serializer_class = CargarInfraccionSerializer
    authentication_classes = [JWTOficialAuth]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        placa_patente = serializer.validated_data.get('placa_patente')
        timestamp = serializer.validated_data.get('timestamp')
        comentarios = serializer.validated_data.get('comentarios')
        
        vehiculo = Vehiculo.objects.get(placa_patente=placa_patente)        
        infraccion = Infraccion.objects.create(
            vehiculo=vehiculo, 
            fecha_infraccion=timestamp, 
            oficial=request.user, 
            observaciones=comentarios)
        
        return Response(
            {
                "mensaje": "la infracción se cargó correctamente.", 
                "infraccion": InfraccionSerializer(infraccion).data
            }, 
            status=status.HTTP_200_OK)
