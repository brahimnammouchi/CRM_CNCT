from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *


class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = rendez_vous
        fields = '__all__'
class AppelTelephoniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model= AppelTelephonique
        fields = '__all__'