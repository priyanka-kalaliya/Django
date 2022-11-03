from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=40)
    image=models.FileField(upload_to='pic')
    price=models.FloatField(null=True)
    description=models.TextField()

    def __str__(self):
        return self.product_name