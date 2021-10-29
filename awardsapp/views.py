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

@login_required(login_url ='accounts/login/')
def profile(request,username):
    title = 'Profile'
    profile = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()
    
    try:
        profile_ifo = Profile.get_by_id(profile.id)
        
    except:
        profile_info = Profile.filter_by_id(profile.id)
        
    projects = Projects.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html',{'title':title,'profile':profile,'projects':projects,'profile_info':profile_info, 'form':form})        
    
    
@login_required(login_url='/accounts/login/')
def update_profile(request):
    profile = User.objects.get(username=request.user) 
    try:
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
        
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(comit = False)
            update.user = request.user
            update.save()
            
            
            return redirect('profile',username=request.user)
        
    else:
        form = ProfileForm()
        
    return render(request,'registration/update_profile.html',{'form':form,'profile_info':profile_info})                   