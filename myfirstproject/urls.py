"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views  #. --> pwd
from .forms import Login,Signup,Forgot,Getotp

urlpatterns = [
    path('admin/', admin.site.urls),  #url for admin panel
    path("",views.index),   #"" --> domain --> localhost
    path("home/",views.home),   #localhost/home/
    path("login/",views.login),  #localhost/users/login --> /users/signin
    path("signup/",views.signup),
    path("aftersignup/",views.aftersignup),
    path("afterlogin/",views.afterlogin.as_view()),
    path("logout/",views.logout),
    path("forgot/",views.forgot),
    path("getotp/",views.getotp),
    path("checkotp/",views.checkotp),
    path("logout/",views.logout),
    path("profile/",views.profile),
    path("delete/<int:id>",views.delete),

    path("users/",include("users.urls")),
    path("blog/",include("blog.urls"))
]
#path(path,function_name)
