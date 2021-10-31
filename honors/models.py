from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    info = models.TextField(max_length=500)
    
    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.save()
    
    def delete_Profile(self):
        self.delete()    
    
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.URLField()
    
    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def all_projects(cls):
        all_projects=cls.objects.all()
        return all_projects
    
    
    @classmethod
    def one_project(cls,id):
        one_project =cls.objects.filter(id=id)
        
        return one_project
    
    
    @classmethod
    def user_project(cls,user):
        user_project =cls.objects.filter(user=user)
        
        return user_project
    
    @classmethod
    def search_project(cls,search_term):
        search_project =cls.objects.filter(title =search_term)
        
        return search_project
    
        
                
    
        