from django.contrib import admin
from .models import Client,Commande,Product, Reclamation


admin.site.register(Commande)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Reclamation)


# Register your models here.
