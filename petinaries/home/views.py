from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProducts

def index(request):
    data=PetProducts.objects.all()
    if "pass" in request.COOKIES:
        a=request.COOKIES["pass"]
        
        return render(request,"index.html",{"pro":data,"cook":a})
    else:
        return render(request,"index.html",{"pro":data})


def register(request):
    if request.method=="POST":
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        username=request.POST["uname"]
        email=request.POST["ename"]
        password=request.POST["pname"]
        repassword=request.POST["re-pname"]
        ucheck=User.objects.filter(username=username)
        
        echeck=User.objects.filter(email=email)

    
        if ucheck:
            msg="username already taken"
            return render(request,"register.html",{"c":msg})

        elif echeck:
            msg="email exist"
            return render(request,"register.html",{"c":msg})

        elif password==" " or password!=repassword:
            msg="password is wrong"
            
            return render(request,"register.html",{"c":msg})

        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save();
            return redirect("/")

    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["pname"]
        check=auth.authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            rep=redirect("/")
            rep.set_cookie("pass",password)
            return rep

        else:
            msg="invalid username or password"
            return render(request,"login.html",{"c":msg})
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    res=redirect("/")
    res.delete_cookie("pass")
    return res

def detail(request):
    return render(request,"detail.html")

def otp(request):

    if request.method=="POST":
        otp=request.POST["oname"]
        ucheck=User.objects.filter(otp=otp)
        if ucheck:
            msg="otp already taken"
            return render(request,"otp.html",{"c":msg})
        else:
            user=User.objects.create_user(otp=otp)
            user.save();
            return redirect("/")

    else:
        return render(request,"otp.html")
 















