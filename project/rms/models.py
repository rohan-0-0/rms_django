from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

class Food(models.Model):
    name = models.CharField(max_length=58)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

class Table(models.Model):
    number = models.CharField(max_length=1)
    is_available = models.BooleanField(default=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
class Order_item(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)