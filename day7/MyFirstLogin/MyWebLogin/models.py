from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    # Author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # image = models.FileField(upload_to='pic',null=True)
    text=models.TextField()
    # email=models.EmailField(null=True)
    
    def __str__(self):
        return self.title