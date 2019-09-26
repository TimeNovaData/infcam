from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    res_user = models.IntegerField(
        verbose_name="ID do Usuário - Odoo"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = "helpdesk"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        permissions = (
            ('tecnico_infcam', 'Fornece acesso de técnico da Infcam'),
        )
