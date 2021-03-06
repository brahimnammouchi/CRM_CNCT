# Generated by Django 4.0.4 on 2022-05-06 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CommercialApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Activités', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='segment_marche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_segment', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='actioncommercial',
            name='commercial',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actioncommercial',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Opportinite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_opportunite', models.CharField(max_length=20)),
                ('reference', models.CharField(max_length=10)),
                ('ca_estime', models.BigIntegerField(blank=True, null=True)),
                ('ca_final', models.BigIntegerField(blank=True, null=True)),
                ('devise', models.CharField(choices=[('1', 'dinars'), ('2', 'euro'), ('3', 'dollar')], default=1, max_length=20)),
                ('phase_de_vente', models.CharField(choices=[('1', 'en cours'), ('2', 'A venir'), ('3', 'En négociation'), ('4', 'Abandonnée'), ('5', 'gagnée'), ('6', 'perdue')], default=1, max_length=20)),
                ('date_signature', models.DateField(verbose_name=django.forms.fields.DateField)),
                ('document_concernee', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommercialApp.client')),
                ('commercial', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
