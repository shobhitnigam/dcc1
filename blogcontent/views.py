from blogcontent.models import newblog
from django.core.checks import messages
from django.urls import reverse
from blogcontent.models import newblog
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def form(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return render(request,'form.html')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    

def tologin(request):
    return render(request,'form.html')


def insertblog(request):
    return render(request,'addblog.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            reg2=newblog.objects.all()
            return render(request,'displayblog.html',{'allblogs':reg2})

            
        else:
            messages.info(request,'invalid details')
            return redirect('tologin')

def blogdisplay(request):
     nblog=request.POST['blogvalue']
     bname=request.POST['blogname']
     reg=newblog(blognew=nblog,name=bname)
     reg.save()
     reg1=newblog.objects.all()
     return render(request,'displayblog.html',{'allblogs':reg1})