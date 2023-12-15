from django.db import models
from brand.models import BrandModel
# Create your models here.
class Car_Model(models.Model):
    file=models.ImageField(upload_to='uploads/')
    car_name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.car_name


class Comment(models.Model):
    car_model=models.ForeignKey(Car_Model,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name