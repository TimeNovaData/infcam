from django.contrib import admin
from .models import Odoo
from .models import OdooParceiro


# Register your models here.
@admin.register(Odoo)
class OdooAdmin(admin.ModelAdmin):
    list_display = ('url', 'db', 'username', 'uid', 'password')


@admin.register(OdooParceiro)
class OdooParceiroAdmin(admin.ModelAdmin):
    list_display = ('id_parceiro', 'user')
