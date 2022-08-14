import datetime
from distutils.command.upload import upload
from distutils.debug import DEBUG
from http import client
from pydoc import importfile
from xmlrpc.client import DateTime
from django.conf import settings
from django.db import models
from django.forms import CharField, DateField
from pkg_resources import to_filename
from CommercialApp.models import Client,Product#,Commande


devise_choice = (
        ("1","dinars"),
        ("2", "euro"),
        ('3', "dollar"),
    )
phase_vente_choice = (
    ("1", "en cours"),
    ("2", "A venir"),
    ("3", "En négociation"),
    ("4", "Abandonnée"),
    ("5", "gagnée"),
    ("6", "perdue")
)

User = settings.AUTH_USER_MODEL 

# Create your models here.
class rendez_vous(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    object=models.CharField(max_length=255)
    date_RendezVous= models.DateTimeField(DateTime, null= True)
class AppelTelephonique(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    datetime= models.DateField(DateTime)
    completed=models.BooleanField(default= False)
    # string representation of the class
    def __str__(self):
     
        #it will return the title
        return str(self.client)
class ActionCommercial(models.Model):

    commercial = models.ForeignKey(User, default=1, null=False, blank=True, on_delete=models.DO_NOTHING)
    #commercial = 
    nom_action = models.CharField(max_length=20)
    CA_esperer = models.IntegerField(blank=True,null=True)
    Cout_action = models.IntegerField(blank=True,null=True)
    But_action = models.CharField(max_length=55)
    debut_action = models.DateTimeField(DateTime)
    echeance = models.DateTimeField(DateTime, null=True)
    completed=models.BooleanField(default= False)
    def __str__(self):
        return str(self.nom_action)
class Opportinite(models.Model):
    commercial = models.ForeignKey(User, default=1, null=False, blank=True, on_delete=models.DO_NOTHING)
    nom_opportunite = models.CharField(max_length=20)
    commercial = models.ForeignKey(User, default=1, null=False, on_delete=models.DO_NOTHING, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reference = models.CharField(max_length=10)
    ca_estime = models.BigIntegerField(blank=True,null=True)
    ca_final = models.BigIntegerField(blank=True, null=True)
    devise = models.CharField(max_length=20, choices= devise_choice, default=1)
    phase_de_vente = models.CharField(max_length=20, choices= phase_vente_choice, default=1)
    date_signature = models.DateField(DateField)
    document_concernee = models.FileField(upload_to='documents/%Y/%m/%d/')
class segment_marche(models.Model):
    nom_segment = models.CharField(null=False, max_length=55)
