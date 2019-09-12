from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cidade
from .models import Empresa
from .models import Endereco
from .models import Estado
from .models import Pais


class EnderecoInline(admin.StackedInline):
    model = Endereco
    fields = [
        'cep',
        'logradouro',
        'complemento',
        'numero',
        'bairro',
        'pais',
        'estado',
        'cidade',
    ]
    exclude = ['data_criacao']
    list_select_related = (
        'pais',
        'estado',
        'cidade',
    )


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf_cnpj']
    exclude = ['user', 'data_criacao']
    inlines = (EnderecoInline,)

    fieldsets = (
        ('Dados Principais', {'fields': (
            'foto',
            'nome',
            'is_empresa',
            'cpf_cnpj',
            'rg'
        )}),
        ('Contato', {'fields': (
            'telefone',
            'celular',
            'email'
        )}),
        ('Detalhes e Configurações', {'fields': (
            'slogan',
        )}),
    )


@admin.register(Cidade)
class CidadeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome', 'estado', 'pais']
    list_filter = ['estado', 'estado__pais']
    readonly_fields = ['data_criacao']


@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome', 'codigo']
    list_filter = ['pais']
    readonly_fields = ['data_criacao']


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    readonly_fields = ['data_criacao']
