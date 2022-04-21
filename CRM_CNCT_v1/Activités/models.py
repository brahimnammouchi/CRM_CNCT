import datetime
from http import client
from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField
from CommercialApp.models import Client,Commande,Product

# Create your models here.
class rendez_vous(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True, default='1')
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    object=models.CharField(max_length=255)
    date_RendezVous= models.DateTimeField(DateTime, null= True)
class AppelTelephonique(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True, default='1')
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    datetime= models.DateField(DateTime)
class ActionCommercial(models.Model):
    #commercial = 
    nom_action = models.CharField(max_length=20)
    CA_esperer = models.IntegerField(blank=True,null=True)
    Cout_action = models.IntegerField(blank=True,null=True)
    But_action = models.CharField(max_length=55)
    debut_action = models.DateTimeField(DateTime)
    echeance = models.DateTimeField(DateTime, null=True)
    