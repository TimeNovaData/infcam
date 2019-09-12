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


class Empresa(Pessoa):
    """
    Classe Empresa implementa as funções relacionadas a empresa gestora da plataforma.
    """

    slogan = models.CharField(
        max_length=200,
        verbose_name="Slogan",
        blank=True
    )

    class Meta:
        app_label = "core"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

