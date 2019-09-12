import requests
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from odoo.models import Odoo
from odoo.models import OdooParceiro
from odoo.api_client.parceiro import get_parceiro, get_id_parceiro


# Create your views here.
def validar_acesso(funcao):
    def validar(*args, **kwargs):
        parceiro = OdooParceiro.objects.filter(user=args[0].user.id).first()

        odoo = Odoo.objects.get(id=1)
        models = odoo.conectar()

        if not parceiro:
            return redirect(reverse_lazy('vincular_usuario'))

        return funcao(
            *args,
            **kwargs,
            parceiro=parceiro,
            odoo=odoo,
            models=models
        )
    return validar


@login_required
def vincular_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        odoo = Odoo.objects.get(id=1)
        models = odoo.conectar()

        if email:
            parceiro = get_id_parceiro(odoo, models, email)

            if parceiro:
                odoo_parceiro = OdooParceiro(user=request.user, id_parceiro=parceiro['id'])
                odoo_parceiro.save()

                data = {
                    'encontrado': True,
                    'resposta': 'Cliente encontrado: ' + parceiro['name']
                }
            else:
                data = {
                    'encontrado': False,
                    'resposta': 'Cliente não encontrado, pesquise novamente!'
                }
            return JsonResponse(data)
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'usuario/index.html')


@login_required
@validar_acesso
def dashboard(request, parceiro, odoo, models):
    return render(
        request,
        'dashboard.html',
        {
            'title': 'Dashboard',
            'parceiro': parceiro,
        }
    )


@login_required
@validar_acesso
def dados_pessoais(request, parceiro, odoo, models):
    pessoa = get_parceiro(odoo, models, parceiro.id_parceiro)

    return render(
        request,
        'dados_pessoais/index.html',
        {
            'title': 'Dados Pessoais',
            'parceiro': parceiro,
            'pessoa': pessoa
        }
    )