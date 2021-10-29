from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

#creating models file
c


class Project(models.Model):
    title = models.Charfield(max_length =50, blank=True)
    image = models.ImageField(upload_to='projectimg/'),default = 'NO IMAGE')
    description = HTMLField()
    link = models.URLField(blank=True)
    User = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null = True, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def  avg_design(self):
        design_reviews = list(map(lambda x:x.design, self.review_set.all()))
        return np.mean(design_reviews)
    
    def avg_content(self):
        content_reviews = list(map(lambda x: x.content, self.review_set.all()))
        return np.mean(usability_reviews)
    def __str__(Self):
        return self.title
    
    @classmethod
    def project_by_id(cls,id):
        project = Project.objects.filter(id = id)
        
        return project
    
    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects
    
    
class Profile(models.Model):
    photo = models.ImageField(upload_to ='profile/',default ='NO PROFILE')
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name ='profile',primary_key=True)  
    contact = models.Charfield(max_length=50,blank=True)
    timestamp = models.DateTimeField(default=timezone.now)  
    
    
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()
    
def __str__(self):
    return self.user.username

@classmethod 
def filter_by_id(cls,id):
    profile = Profile.objects.filter(user = id).first()
    return profile          


class Review(models.Model):
    REVIEW_CHOICES =(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (4,'5'),                            
    )
    
design = models.IntegerField(choices= REVIEW_CHOICES,default =0, blank=False)
usability = models.IntegerField(choices = REVIEW_CHOICES,default =0,blank = False)
content = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=40)
project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
timestamp = models.DateTimeField(auto_now_add=True)
user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)


def __str__(self):
    return self.user