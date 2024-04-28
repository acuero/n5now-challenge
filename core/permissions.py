"""
Clase con clase autenticadora personalizada para Oficiales.
"""
from rest_framework.permissions import BasePermission
from core.management.authentication import JWTOficialAuth
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class OficialIsAuthenticated(BasePermission):
    """
    Clase tipo BasePermission que utilizará un endpoint para otorgar acceso.
    """
    def has_permission(self, request, view):
        """
        Permiso que determina si otorga el permiso a un oficial a acceder a un recurso.
        """        
        jwt_auth = JWTOficialAuth()
        try:
            oficial, _ = jwt_auth.authenticate(request)
        except AuthenticationFailed:
            return False 

        if oficial.usuario.is_active:
            return True
        else:
            return False
