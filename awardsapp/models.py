from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creating models file
class Project(midels.Model):
    title = models.Charfield(max_length =50, blank=True)
    image = models.ImageField(upload_to'projectimg/'),default = 'NO IMAGE')
    description = HTMLField()
    link = models.URLField(blank=True)
    User = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null = True, on_delete = models.CASCADE)
    timestamp = models.DateTimeFiels(auto_now_add = True)
    
    