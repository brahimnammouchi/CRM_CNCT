from django.contrib import admin
from django.urls import path, include
from CommercialApp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
     #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    # GET PUT DELETE from rest framwork function based view @api_view
    path('rest/fbv/<id>', views.FBV_pk),
    #path('api/', include('CommercialApp.urls')),
    path('rest/cbv/<int:id>', views.CBV_pk.as_view()),


]
