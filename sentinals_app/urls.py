from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('roster', views.roster),
    path('schedule', views.schedule),
]
