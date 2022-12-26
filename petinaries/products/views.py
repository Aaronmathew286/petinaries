from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import PetProducts
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail




def detail(request):
    id=request.GET["id"]

    data=PetProducts.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)

    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)
            request.session["his"].insert(0,id)
        else:
            request.session["his"].insert(0,id)
        if len(request.session["his"])>4:
            request.session["his"].pop()

        print(request.session["his"])
        prop=PetProducts.objects.filter(id__in=request.session["his"])
        print(prop)
        request.session.modified=True
        return render(request,"detail.html",{"pro":data,"total":total,"abc":prop})
    else:
        print("hello")
        request.session["his"]=[id]
        return render(request,"detail.html",{"pro":data,"total":total})


def detail2(request):
    id=request.GET["id"]
    if cache.get(id):
        print("data from cache")
        data=cache.get(id)
    else:
        print("data from database")
        data=PetProducts.objects.get(id=id)
        cache.set(id,data)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    return render(request,"detail.html",{"pro":data,"total":total})

def email(request):
    email_from=settings.EMAIL_HOST_USER
    email_to=["aaronmathew268@gmail.com",]
    subject="product"
    message="hello hgbdgwukyhgb"
    send_mail(subject,message,email_from,email_to)
    return render(request,"test.html")




