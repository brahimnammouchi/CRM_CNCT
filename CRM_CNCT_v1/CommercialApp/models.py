from http import client
from multiprocessing.sharedctypes import Value
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client (models.Model):
    id_client=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    MatruculeFiscal= models.CharField(max_length=10)
    adresse=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    numero=models.IntegerField()

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image=models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
class Commande(models.Model):
    client = models.ForeignKey(Client, related_name='commande', on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, related_name='commande', on_delete=models.CASCADE)
    qte = models.IntegerField()