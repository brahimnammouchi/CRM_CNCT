# Generated by Django 3.1.7 on 2022-04-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0007_auto_20220405_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='id_command',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
