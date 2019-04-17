from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.TextField(blank=True)
    sku=models.TextField(blank=True)
    description=models.TextField(blank=True)
    flag=models.CharField(max_length=50,blank=True)