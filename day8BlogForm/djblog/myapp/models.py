from distutils.command import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    image = models.FileField(upload_to='pic',null=True)
    created_on=models.DateTimeField(auto_now_add=TRUE,null=TRUE)

    def __str__(self):
        return self.title