"""
Clase con clase autenticadora personalizada para Oficiales.
"""
from rest_framework.permissions import BasePermission
from core.management.authentication import JWTOficialAuth
from rest_framework.exceptions import AuthenticationFailed


class OficialIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        jwt_auth = JWTOficialAuth()
        try:
            oficial, _ = jwt_auth.authenticate(request)
        except AuthenticationFailed:
            return False 

        if oficial.usuario.is_active:
            return True
        else:
            return False
