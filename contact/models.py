from django.db import models
import datetime
# Create your models here.

class Messages(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=250)
    MsgSubject = models.TextField(null= True)
    MsgBody = models.TextField()
    DateSent = models.DateField(auto_now_add=True)

class Subscription(models.Model):
    SubcriberName = models.CharField(max_length=100)
    SubcriberEmail = models.EmailField(max_length=250,unique=True)
    DateOnSubscribe = models.DateField(auto_now_add=True)

    