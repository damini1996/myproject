from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include,url
from users.models import Adduser


urlpatterns = [
    path("",views.index),  #"" --> localhost/blog/
    path("addblog/",views.addblog),
    path("addpost/",views.addpost.as_view()),
    path("myblog/",views.myblog),
    path("profile/",views.profile),
    path("allblogs/",views.allblogs),
    path("delete/<int:id>",views.delete),
]