from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home,name = "home"),
    path("", views.home,name = "data_set"),
    path("features", views.features,name = "features"),
    path("featuresSerie", views.featuresSerie,name = "featuresSerie"),
   
    #path("toppings/")views.logout_view, name="toppings")
]
