__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .pessoa import Pessoa
from .cidade import Cidade
from .estado import Estado
from .pais import Pais
from core.managers import EnderecoManager
from datetime import datetime


class Endereco(models.Model):
    """
    Classe Endereco implementa as funções relacionadas a um endereço na plataforma.
    """

    logradouro = models.CharField(
        max_length=200,
        verbose_name="Logradouro"
    )

    complemento = models.CharField(
        max_length=100,
        verbose_name="Complemento",
        blank=True
    )

    numero = models.CharField(
        max_length=10,
        verbose_name="Número"
    )

    bairro = models.CharField(
        max_length=200,
        verbose_name="Bairro"
    )

    cep = models.CharField(
        max_length=9,
        verbose_name="CEP"
    )

    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Cidade"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Estado"
    )

    pais = models.ForeignKey(
        Pais,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="País"
    )

    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Pessoa"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    objects = EnderecoManager()

    def __str__(self):
        return self.logradouro

    class Meta:
        app_label = "core"
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

