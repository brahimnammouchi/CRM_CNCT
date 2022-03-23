from http import client
from multiprocessing.connection import Client
from urllib import request
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from CommercialApp.models import Client,Commande,Product
from .serializers import ClientSerializer,ProductSerializer,CommandSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
#1 without REST and no model query FBV
def no_rest_no_model(request):
    clients = [
        {
            'id': 1,
            "Name": "Omar",
            "mobile": 789456,
            "MatruculeFiscal":"B28272",
            'adresse':"dshsh",
            'email':'sv@test.com',
            'numero':273713
        },
        {
            'id': 2,
            "Name": "diaa",
            "mobile": 789456,
            "MatruculeFiscal":"g4455",
            'adresse':"rgt",
            'email':'yy@test.com',
            'numero':3288
        }
    ]
    return JsonResponse (clients, safe=False)
###########
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request, *args, **kwargs):
    pk = kwargs.get('pk')

    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

#PUT
    elif request.method == 'PUT':
        serializer = ClientSerializer(client,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method == 'DELETE':
        client.delete()
        return Response(status.HTTP_204_NO_CONTENT)