from django.urls import include, path
from core import views

urlpatterns = [
    path("token/", views.ObtenerTokenView.as_view(), name='obtener_token'),
    path("cargar_infraccion/", views.CargarInfraccionView.as_view(), name='cargar_infraccion'),
    path("generar_informe/", views.GenerarInformeView.as_view(), name='generar_informe'),
]
