from django.db import router
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
<<<<<<< Updated upstream
from .views import API_RDV, ActionCom_ViewSet, AppelTel_ViewSet, Opportinite_ViewSet, SegmentMarche_ViewSet
=======
from .views import API_RDV, ActionCom_ViewSet, AppelTel_ViewSet
>>>>>>> Stashed changes
from django.urls import path, include
router = DefaultRouter()
router.register('AppelTel',AppelTel_ViewSet)
router.register('Action',ActionCom_ViewSet)
<<<<<<< Updated upstream
router.register('Opportinite',Opportinite_ViewSet)
router.register('SegmentMarche', SegmentMarche_ViewSet)
=======
>>>>>>> Stashed changes
#router.register('RDV',API_RDV.as_view())

urlpatterns= [
    path ( 'api/', include(router.urls))
    
]