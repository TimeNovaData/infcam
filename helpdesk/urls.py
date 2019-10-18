from django.contrib import admin
from django.urls import path, include
from .views import (
    vincular_usuario,
    criar_usuario,
    dashboard_cliente,
    dados_pessoais,
    novo_reparo,
    dashboard_tecnico,
    detalhar_reparo,
    adicionar_anexo,
    alterar_estagio,
    adicionar_produto,
    adicionar_servico,
    adicionar_laudo,
    adicionar_nota
)

urlpatterns = [
    path('', dashboard_cliente, name='dashboard_cliente'),
    path('dashboard_tecnico/', dashboard_tecnico, name='dashboard_tecnico'),
    path('reparo/<int:reparo>', detalhar_reparo, name='detalhar_reparo'),
    path('reparo/adicionar_anexo/<int:reparo>', adicionar_anexo, name='adicionar_anexo'),
    path('reparo/alterar_estagio/<int:reparo>', alterar_estagio, name='alterar_estagio'),
    path('reparo/adicionar_produto/<int:reparo>', adicionar_produto, name='adicionar_produto'),
    path('reparo/adicionar_servico/<int:reparo>', adicionar_servico, name='adicionar_servico'),
    path('reparo/adicionar_laudo/<int:reparo>', adicionar_laudo, name='adicionar_laudo'),
    path('reparo/adicionar_nota/<int:reparo>', adicionar_nota, name='adicionar_nota'),
    path('usuario/', vincular_usuario, name='vincular_usuario'),
    path('criar_usuario/', criar_usuario, name='criar_usuario'),
    path('dados_pessoais/', dados_pessoais, name='dados_pessoais'),
    path('novo_reparo/', novo_reparo, name='novo_reparo'),
]
