from django.db import models
from django.contrib.auth.models import User

class Thoughts(models.Model):
    title = models.CharField(max_length = 150)
    content = models.CharField(max_length = 400)
    date_posted = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,max_length = 10, on_delete = models.CASCADE,null = True)

class Profile(models.Model):
    profile_pic = models.ImageField(null=True,blank=True,default='user.png')
    user = models.ForeignKey(User,max_length=10,on_delete=models.CASCADE)