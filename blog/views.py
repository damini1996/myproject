from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Addblogs
from users.models import Adduser
from .models import Addblog
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:red'>Welcome to my blog app</h1>")

def addblog(request):
    form = Addblogs()
    return render(request,"addblog.html",{'form':form})

class addpost(View):
    def get(self,request):
        error = "Blog is invalid"
        form = Addblogs()
        return render(request,"addblog.html",{'form':form ,'error':error})
        
    def post(self,request):
        form = Addblogs(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            user = Adduser.objects.get(email=request.session.get("email"))
            Addblog.objects.create(title=title,post=post,user=user)
            error = "Blog added"
            return render(request,"afterlogin.html",{'error':error})

def myblog(request):
    if request.method == "GET":
        user = Adduser.objects.get(email=request.session.get("email"))
        blogs = Addblog.objects.filter(user=user.id)
        values = []
        for i in blogs:
            d = {
                "title" : i.title,
                "post"  : i.post,
                "user"  : i.user.fullname,
                "date"  : i.date
            }
            values.append(d)
        return render(request,"userblogs.html",{"blogs":values})
    else:
        error = "User post not found"
        return render(request,"afterlogin.html",{'error':error})

def allblogs(request):
    if request.method == "GET":
        allblog = Addblog.objects.all()[:10]
        values = []
    for i in allblog:
        d = {
                "title": i.title,
                "post" : i.post,
                "user" : i.user.fullname,
                "date" : i.date
        }
        values.append(d)
    return render(request,"userblogs.html",{'blogs':values})

def profile(request):
    displayuser = Adduser.objects.all()
    return render(request,"profile.html",{"Adduser":displayuser})

def delete(request, id):
    displayuser = Adduser.objects.get(id=id)
    print(type(displayuser))
    displayuser.delete() # change here
    return redirect("/myblog")
    

    
    








