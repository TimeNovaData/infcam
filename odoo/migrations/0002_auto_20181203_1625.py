# Generated by Django 2.1.3 on 2018-12-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odoo',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='odoo',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Username'),
        ),
    ]
