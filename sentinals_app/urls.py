from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('home', views.index),
    path('roster', views.roster),
    path('schedule', views.schedule),
]
