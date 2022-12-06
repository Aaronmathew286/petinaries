from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request,"index.html")



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
            return redirect("/")
        else:
            msg="invalid username or password"
            return render(request,"login.html",{"c":msg})
    else:
        return render(request,"login.html")















