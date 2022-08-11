from http import client
from multiprocessing.sharedctypes import Value
from pyexpat import model
from tkinter import CASCADE
from urllib import request
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client (models.Model):
    nom = models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    MatruculeFiscal= models.CharField(max_length=10)
    adresse=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    def __str__(self):
        #it will return the title
        return self.nom

class Product(models.Model):
    #id_product=models.AutoField(blank=True,primary_key=True)
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image=models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        #it will return the title
        return self.name
class Commande(models.Model):
    id_command= models.AutoField(primary_key=True,auto_created=True, default='1')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, related_name='commande', on_delete=models.CASCADE)
    qte = models.IntegerField()
    def __str__(self):
        #it will return the title
        return str(self.id_command)