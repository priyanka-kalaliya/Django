from django.db import models

# Create your models here.
class post(models.Model):
    tittle=models.CharField(max_length=100)
    text=models.TextField()
    email=models.EmailField(null=True)
    
    def __str__(self):
        return self.tittle



class student_info(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    marks = models.IntegerField()

    def __str__(self):
        return self.name