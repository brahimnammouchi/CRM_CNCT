from django.contrib import admin
from django.urls import path, include
from CommercialApp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from Activités import views as views2

router = DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
     #CRUD API CLIENT
    path('rest/cbv/<int:id>', views.CBV_pk.as_view()),
    path('rest/apiproduct/<int:id_product>', views.ApiProduct.as_view()),
    path('REST/RDVAPI/<int:id>', views2.API_RDV.as_view()),

]
