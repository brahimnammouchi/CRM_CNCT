# Generated by Django 4.0.4 on 2022-08-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activités', '0003_appeltelephonique_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actioncommercial',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
