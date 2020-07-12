from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length= 60)
    description= models.TextField()
    user = models.ManyToManyField(User,related_name='message')
    