from django.http import JsonResponse
from django.core import serializers
from .models import Endereco
from .models import Estado
from .models import Cidade


def buscar_cep(request):
    if request.method == 'POST':
        cep = request.POST.get('cep', "")

        endereco = Endereco.objects.buscar_cep(cep)

        return JsonResponse(endereco)


def on_change_pais(request):
    if request.method == 'POST':
        pais = request.POST.get('pais', 0)

        estados = Estado.objects.filter(pais=pais)

        estados_serializados = serializers.serialize('json', estados)
        return JsonResponse(estados_serializados, safe=False)


def on_change_estado(request):
    if request.method == 'POST':
        estado = request.POST.get('estado', 0)

        cidades = Cidade.objects.filter(estado=estado)

        cidades_serializadas = serializers.serialize('json', cidades)
        return JsonResponse(cidades_serializadas, safe=False)
