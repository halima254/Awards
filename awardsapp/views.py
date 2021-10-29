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

   
@login_required(login_url='/accounts/login')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
        
			return redirect('index')
	else:
			form = ProjectForm()
            
	return render(request, 'project.html',{"form":form})      

@login_required(login_url='/accounts/login')
def project_details(request,id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.order_by('-timestamp')

    context={"project":project,"reviews":reviews}
    return render(request, 'project_details.html',context)  

@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
          

            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Review()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (review.design + review.usability + review.content)/3
            review.save()
            # return redirect('index')
            return HttpResponseRedirect(reverse('projectdetails', args=(project.id,)))
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"user":current_user,"project":proj,"form":form})   

def review_list(request):
    latest_review_list = Review.objects.order_by('-timestamp')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)   

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})
