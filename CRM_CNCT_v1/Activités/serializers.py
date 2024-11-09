from dataclasses import field, fields
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
class ActioncommercialSerializer(serializers.ModelSerializer):
    class Meta:
        model= ActionCommercial
        fields = '__all__'
class opportiniteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Opportinite
        fields = '__all__'
class SegmentMarcheSerializer(serializers.ModelSerializer):
     class Meta:
        model = segment_marche
        fields = '__all__'
