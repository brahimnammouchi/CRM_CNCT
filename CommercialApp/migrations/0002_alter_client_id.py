# Generated by Django 4.0.4 on 2022-08-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]