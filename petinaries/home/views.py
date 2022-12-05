from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request,"index.html")

def test(request):
    val="Python"
    val2="java"
   
    return render(request,"test.html",{"a":val,"b":val2})

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def sub(request):
    username=request.GET["uname"]
    password=request.GET["pname"]
    check=auth.authenticate(username=username,password=password)
    if check is not None:
        auth.login(request,check)
        return redirect("/")
    else:
        msg="invalid username or password"
        return render(request,"test.html",{"c":msg})

def reg2(request):
    firstname=request.GET["fname"]
    lastname=request.GET["lname"]
    username=request.GET["uname"]
    email=request.GET["ename"]
    password=request.GET["pname"]
    repassword=request.GET["re-pname"]
    ucheck=User.objects.filter(username=username)
    
    echeck=User.objects.filter(email=email)

    
    if ucheck:
        msg="username already taken"
        return render(request,"test.html",{"c":msg})

    elif echeck:
        msg="email exist"
        return render(request,"test.html",{"c":msg})

    elif password==" " or password!=repassword:
        msg="password is wrong"
        
        return render(request,"test.html",{"c":msg})

    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save();
        return redirect("/")









