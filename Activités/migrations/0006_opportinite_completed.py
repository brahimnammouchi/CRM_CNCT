# Generated by Django 4.0.4 on 2022-09-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activités', '0005_rendez_vous_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportinite',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
