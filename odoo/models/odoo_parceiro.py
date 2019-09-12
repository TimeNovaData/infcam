__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2018, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from django.contrib.auth.models import User


class OdooParceiro(models.Model):
    """
    Classe Odoo Parceiro armazena os dados do parceiro no Odoo.
    """
    id_parceiro = models.IntegerField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id_parceiro)

    class Meta:
        app_label = "odoo"
        verbose_name = "Parceiro Odoo"
        verbose_name_plural = "Parceiros Odoo"

