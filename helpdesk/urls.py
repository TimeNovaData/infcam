from django.contrib import admin
from django.urls import path, include
from .views import (
    vincular_usuario,
    dashboard,
    dados_pessoais,
)

urlpatterns = [
    path('', dashboard, name='index'),
    path('usuario/', vincular_usuario, name='vincular_usuario'),
    path('dados_pessoais/', dados_pessoais, name='dados_pessoais'),
]
