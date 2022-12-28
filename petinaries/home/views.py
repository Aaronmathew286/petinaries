from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProducts
from django.conf import settings
from django.core.mail import send_mail


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
           
            
            rep=render(request,"otp.html")
            rep.set_cookie("pass",password)
            rep.set_cookie("username",username)
            rep.set_cookie("firstname",firstname)
            rep.set_cookie("lastname",lastname)
            rep.set_cookie("email",email)
            #otp creation
            l1=len(username)
            l2=len(password)
            l3=l1+l2*54321
            l4=str(l3)[:5]
            send_mail("otp validation",f"Your otp is {l4}",settings.EMAIL_HOST_USER,[email,])
            return rep
            #user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            #user.save();


            

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
        username=request.COOKIES["username"]
        password=request.COOKIES["pass"]
        otp=request.POST["oname"]
        l1=len(username)
        l2=len(password)
        l3=l1+l2*54321
        l4=str(l3)[:5]

        if otp==l4:
            username=request.COOKIES["username"]
            password=request.COOKIES["pass"]
            firstname=request.COOKIES["firstname"]
            lastname=request.COOKIES["lastname"]
            email=request.COOKIES["email"]
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save();
            auth.login(request,user)
            return redirect("/")

        else:
            return render(request,"otp.html")
    else:
        return render(request,"otp.html")
 
def search(request):
    return render(request,"search.html")

















