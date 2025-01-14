# firmas/urls.py
from django.urls import path
from .views.validar_firma import validar_firma
from .views.login import login
from .views.registro import registro
from .views.firma import home 

app_name = "firmas"

urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('home/', home, name='home'),
    path('descargar/', home, name='descargar'),
    path('validar_firma/', validar_firma, name='validar_firma'),
]