from django.shortcuts import render, redirect,get_object_or_404
from awardsapp.models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from awardsapp.forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *




# Create your views here.


def signup(request):
    if request.method =='POST':
        form = SignupForm
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
        
    else:
        form = SignupForm()
    return render (request, 'registration/reg.html',{'form':form})        


@login_required(login_url ='/accounts/login/')
def index(request):
    message = "welcome to the awwards"
    
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()
    
    context ={'profiles':profiles,'projects':projects,'reviews':reviews,'message':message}
    return render(request,'index.html',context)