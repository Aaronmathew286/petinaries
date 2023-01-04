from django.urls import path
from . import views



urlpatterns = [  
  
    path("",views.detail2,name="detail"),
    path("test/",views.email,name="mailpage"),
    path("auto/",views.autosearch,name="autopage"),
    path("checkout/",views.checkout,name="checkpage"),

]