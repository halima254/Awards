from django import forms
from .models import Project,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','project_id']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

