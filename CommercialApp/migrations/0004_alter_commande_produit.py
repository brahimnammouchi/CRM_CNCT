# Generated by Django 4.0.4 on 2022-08-12 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0003_remove_product_id_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommercialApp.product'),
        ),
    ]