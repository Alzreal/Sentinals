from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('sentinals_app.urls')),
]
