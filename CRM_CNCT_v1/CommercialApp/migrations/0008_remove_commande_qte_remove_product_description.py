# Generated by Django 4.0.4 on 2022-08-12 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0007_rename_id_command_commande_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='qte',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
