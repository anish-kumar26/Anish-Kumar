# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    age = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

class OrderStatus(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    placed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
