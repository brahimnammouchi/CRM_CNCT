from webbrowser import get
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from .models import rendez_vous
from .serializers import RendezVousSerializer

# API RendezVous
class API_RDV(APIView):
    def queryset_Rdv(self, id):
        try:
            return rendez_vous.objects.get(id = id)
        except rendez_vous.DoesNotExist:
            raise Http404
    def get(self, request, id):
        rdv = self.queryset_Rdv(id)
        serializer = RendezVousSerializer(rdv)
        return Response(serializer.data)
    def put(self, request, id):
        rdv = self.queryset_Rdv(id)
        serializer = RendezVousSerializer(rdv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, id):
        rdv = self.queryset_Rdv(id)
        rdv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      ######### API APPEL TELEPHONIQUE  

    