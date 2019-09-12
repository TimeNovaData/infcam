__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from datetime import datetime
import xmlrpc.client


class Odoo(models.Model):
    """
    Classe Odoo armazena os dados da instância do Odoo.

    Armazena os dados da instância do Odoo para comunicação com o Webservice.
    """

    url = models.CharField(
        max_length=250,
        null=False,
        verbose_name="URL"
    )

    db = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Banco de Dados"
    )

    username = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Username"
    )

    uid = models.IntegerField(
        null=False,
        verbose_name="ID de Usuário"
    )

    password = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Password"
    )

    def __str__(self):
        return self.url

    class Meta:
        app_label = "odoo"
        verbose_name = "Odoo"
        verbose_name_plural = "Odoo"
        ordering = ['url']

    def conectar(self):
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

        return models



