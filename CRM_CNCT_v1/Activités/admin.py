from django.contrib import admin

from .models import AppelTelephonique, rendez_vous

# Register your models here.
admin.site.register(rendez_vous)
class adminAppelTel(admin.ModelAdmin):
    listdisplay =("client", "datetime", "completed")
admin.site.register(AppelTelephonique,adminAppelTel)
