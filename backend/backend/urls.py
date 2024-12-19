
# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from todo import views                            # add this
        
router = routers.DefaultRouter()                      # add this
router.register(r'acceptUser', views.AcceptUser, 'accept')     # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/acceptUser', views.AcceptUser),
 #   path('api/acceptUser', views.AcceptUser, name='accept'),
]