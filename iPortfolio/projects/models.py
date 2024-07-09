from django.db import models
from datetime import datetime
# Create your models here.

class Projects(models.Model):
    data = [
        ("web", "web"),
        ("game", "game"),
        ("Ai", "Ai"),
        ("Blockchain", "Blockchain"),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    descripe = models.TextField(blank=True, null=True, verbose_name='description')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=data, blank=True, null=True, )
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return (self.title)
    
    class Meta:
        verbose_name = 'project'

class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return (self.title)
    
    class Meta:
        verbose_name = 'Customer'