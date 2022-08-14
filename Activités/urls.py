from django.db import router
from django.contrib import admin
from django.urls import URLPattern
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import ActionCom_ViewSet, AppelTel_ViewSet, Opportinite_ViewSet, SegmentMarche_ViewSet
from .views import RDV_ViewSet, ActionCom_ViewSet, AppelTel_ViewSet
from Activités import views
from CommercialApp import views as views2
from django.urls import path, include
router = DefaultRouter()
router.register(r'AppelTel',views.AppelTel_ViewSet, 'AppelTel')
router.register(r'Action',ActionCom_ViewSet)
router.register(r'Opportinite',Opportinite_ViewSet)
router.register(r'SegmentMarche', SegmentMarche_ViewSet)
router.register(r'Client', views2.Client_ViewSet)
router.register(r'Produit', views2.Product_ViewSet) 
router.register(r'Commande', views2.Commande_ViewSet)
#router.register(r'Client',ClientSerializer)

#router.register('RendezVous',RDV_ViewSet )

#router.register('RDV',API_RDV.as_view())

urlpatterns= [
    path ( 'api/', include(router.urls)),
    path('admin/', admin.site.urls),

    
]