# Generated by Django 4.0.4 on 2022-08-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0013_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]