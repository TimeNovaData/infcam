from django.contrib import admin
from django.urls import path, include
from .views import (
    vincular_usuario,
    dashboard_cliente,
    dados_pessoais,
    novo_reparo
)

urlpatterns = [
    path('', dashboard_cliente, name='dashboard_cliente'),
    path('usuario/', vincular_usuario, name='vincular_usuario'),
    path('dados_pessoais/', dados_pessoais, name='dados_pessoais'),
    path('novo_reparo/', novo_reparo, name='novo_reparo'),
]
