__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Pessoa(models.Model):
    """
    Classe Pessoa implementa as funções relacionadas a uma pessoa da plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    is_empresa = models.BooleanField(
        verbose_name="É uma empresa?",
        default=False
    )

    cpf_cnpj = models.CharField(
        max_length=18,
        verbose_name="CPF/CNPJ"
    )

    rg = models.CharField(
        max_length=30,
        verbose_name="RG",
        blank=True,
        null=True
    )

    telefone = models.CharField(
        max_length=30,
        verbose_name="Telefone",
        blank=True,
        null=True
    )

    celular = models.CharField(
        max_length=30,
        verbose_name="Celular"
    )

    email = models.CharField(
        max_length=150,
        verbose_name="Email"
    )

    foto = models.ImageField(
        verbose_name="Foto",
        blank=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="User"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data",
        default=datetime.now
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

