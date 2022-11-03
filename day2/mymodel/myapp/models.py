from django.db import models

# Create your models here.

class post(models.Model):
    tittle=models.CharField(max_length=100)
    text=models.TextField()
    email=models.EmailField(null=True)
    
    def __str__(self):
        return self.tittle

