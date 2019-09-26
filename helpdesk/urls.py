from django.contrib import admin
from django.urls import path, include
from .views import (
    vincular_usuario,
    dashboard_cliente,
    dados_pessoais,
    novo_reparo,
    dashboard_tecnico,
    detalhar_reparo,
    adicionar_anexo,
    alterar_estagio
)

urlpatterns = [
    path('', dashboard_cliente, name='dashboard_cliente'),
    path('dashboard_tecnico/', dashboard_tecnico, name='dashboard_tecnico'),
    path('reparo/<int:reparo>', detalhar_reparo, name='detalhar_reparo'),
    path('reparo/adicionar_anexo/<int:reparo>', adicionar_anexo, name='adicionar_anexo'),
    path('reparo/alterar_estagio/<int:reparo>', alterar_estagio, name='alterar_estagio'),
    path('usuario/', vincular_usuario, name='vincular_usuario'),
    path('dados_pessoais/', dados_pessoais, name='dados_pessoais'),
    path('novo_reparo/', novo_reparo, name='novo_reparo'),
]
