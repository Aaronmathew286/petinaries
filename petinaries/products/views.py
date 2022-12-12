from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import PetProducts




def detail(request):
    id=request.GET["id"]

    data=PetProducts.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    return render(request,"detail.html",{"pro":data,"total":total})


