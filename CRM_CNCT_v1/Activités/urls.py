from django.db import router
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from .views import API_RDV, AppelTel_ViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('AppelTel',AppelTel_ViewSet)
#router.register('RDV',API_RDV.as_view())

urlpatterns= [
    path ( 'api/', include(router.urls))
    
]