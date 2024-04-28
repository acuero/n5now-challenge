"""
Clase que gestiona la autenticación de oficiales mediante tokens.
"""

from datetime import datetime, timedelta

import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError
from core.models.oficial import Oficial


class JWTOficialAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        """
        Implementacion de la autenticación
        """        
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None

        jwt_token = JWTOficialAuth.obtener_token_del_header(jwt_token)
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()

        nui_oficial = payload.get('nui')
        if nui_oficial is None:
            raise AuthenticationFailed('Número único de identificación del oficial no encontrado.')

        oficial = Oficial.objects.filter(nui=nui_oficial).first()
        if oficial is None:
            raise AuthenticationFailed('Oficial no encontrado')
        return oficial, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def crear_jwt(cls, oficial):
        payload = {
            'nui': oficial.nui,
            'expiracion': int((datetime.now() + timedelta(minutes=settings.JWT_CONF.get('TOKEN_LIFETIME_MINUTES'))).timestamp()),
            'generado': datetime.now().timestamp(),
            'nombre': oficial.nombre
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return jwt_token

    @classmethod
    def obtener_token_del_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')
        return token
