from django.urls import path
from . import views
from . import feed


urlpatterns = [

    path("",views.index,name="homepage"),

    path("register/",views.register,name="registerpage"),
    path("login",views.login,name="loginpage"),
    path("logout",views.logout,name="logoutpage"),
    path("otp/",views.otp,name="otppage"),
    path("search/",views.search,name="searchpage"),
    path("feed/",feed.latestproduct()),


]