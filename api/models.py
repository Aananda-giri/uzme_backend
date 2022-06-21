from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
from django.db.models.signals import post_save 

class Post(models.Model):#TimeStampedModel):
    title = models.CharField(max_length=512) 
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_subscribers(self): 
        users = User.objects.all() 
        users = users.exclude(pk=self.author.pk) 
        return users