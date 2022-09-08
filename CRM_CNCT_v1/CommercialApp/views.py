from http import client
from itertools import product
from multiprocessing.connection import Client
from urllib import request, response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from CommercialApp.models import Client,Commande,Product
from .serializers import ClientSerializer,ProductSerializer,CommandSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from.models import Client,Commande,Product
from rest_framework.viewsets import ModelViewSet

    
    #########################
# class  CBV_pk(APIView):
    
#     def get_object(self, id):
#         try:
#             return Client.objects.get(id=id)
#         except Client.DoesNotExists:
#             raise Http404
#     def get(self, request, id):
#         client = self.get_object(id)
#         serializer = ClientSerializer(client)
#         return Response(serializer.data)
#     def put(self, request, id):
#         client = self.get_object(id)
#         serializer = ClientSerializer(client, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id):
#         client = self.get_object(id)
#         client.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class Client_ViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
#CRUD Product
# class ApiProduct(APIView):
#     def get_object(self,id_product):
#         try:
#             return Product.objects.get(id_product=id_product)
#         except Product.DoesNotExist:
#             raise Http404
#     def get(self, request, id_product):
#         product = self.get_object(id_product)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self,request, id_product):
#         product= self.get_object(id_product)
#         serializer= ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id_product):
#         product= self.get_object(id_product)
#         product.delete()
class Product_ViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
##CRUD COMMAND
# class ApiCommand(APIView):
#     def get_object(self,id_command):
#         try:
#             return Commande.objects.get(id_command= id_command)
#         except Commande.DoesNotExist:
#             raise Http404
#     def get(self, request, id_command):
#         commande= self.get_object(id_command)
#         serializer= CommandSerializer(commande)
#         return Response(serializer.data)
#     def put(self, request, id_command):
#         commande= self.get_object(id_command)
#         serializer= CommandSerializer(commande, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id_command):
#         commande=self.get_object(id_command)
#         commande.delete()
class Commande_ViewSet(ModelViewSet):
    serializer_class = CommandSerializer
    queryset = Commande.objects.all()

