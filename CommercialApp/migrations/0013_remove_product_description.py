# Generated by Django 4.0.4 on 2022-08-12 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0012_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
