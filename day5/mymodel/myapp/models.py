from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    Author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text=models.TextField()
    # email=models.EmailField(null=True)
    
    def __str__(self):
        return self.title



class student_info(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    marks = models.IntegerField()

    def __str__(self):
        return self.name