from django.urls import path
from . import views



urlpatterns = [  
  
    path("",views.detail2,name="detail"),
    path("test/",views.email,name="mailpage"),

]