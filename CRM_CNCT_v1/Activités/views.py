from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from .models import ActionCommercial, AppelTelephonique, Opportinite, rendez_vous, segment_marche
from .serializers import ActioncommercialSerializer, AppelTelephoniqueSerializer, RendezVousSerializer, SegmentMarcheSerializer, opportiniteSerializer
from .models import ActionCommercial, AppelTelephonique, rendez_vous
from .serializers import ActioncommercialSerializer, AppelTelephoniqueSerializer, RendezVousSerializer

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
    
    def post(self, request, *args, **kwargs):
        rdv_data = request.data
        new_rdv = rendez_vous.objects.create()
        new_rdv.save()
        serializer = RendezVousSerializer(new_rdv)
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
#class API_AppelTel(APIView):
 #   def get_object(self, id):
  #      try:
   #         return AppelTelephonique.objects.get(id = id)
   ###     except AppelTelephonique.DoesNotExist:
 #           raise Http404
    #def get(self, request, id):
     #   appeltel = self.get_object(id)
#        serializer = AppelTelephoniqueSerializer(appeltel)
      #  return Response(serializer.data)
    #def post(self, request, *args, **kwargs):
     #   appel_data= request.data
      #  new_appel= AppelTelephonique.objects.create()
       # new_appel.save()
        #serializer = AppelTelephoniqueSerializer(new_appel)
        #return Response(serializer.data)
#    def put(self, request, id):
#        appeltel = self.appeltel(id)
#        serializer = AppelTelephoniqueSerializer(appeltel, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    def delete(self,request, id):
#        appeltel = self.queryset_Rdv(id)
#        appeltel.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
class AppelTel_ViewSet(ModelViewSet):
    serializer_class = AppelTelephoniqueSerializer
    queryset = AppelTelephonique.objects.all()
#API Action Commercial
class ActionCom_ViewSet(ModelViewSet):
    serializer_class = ActioncommercialSerializer
    queryset = ActionCommercial.objects.all()
class Opportinite_ViewSet(ModelViewSet):
    serializer_class = opportiniteSerializer
    queryset = Opportinite.objects.all()
class SegmentMarche_ViewSet(ModelViewSet):
    serializer_class = SegmentMarcheSerializer
    queryset = segment_marche.objects.all()

