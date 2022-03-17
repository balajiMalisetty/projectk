from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    height = models.IntegerField(default=0,null=True,blank=True)
    weight = models.IntegerField(default=0,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    calories = models.IntegerField(default=0,null=True,blank=True)
    mobile = models.CharField(max_length=10,null=True,blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.calories = 88 + (14*self.weight) + (5*self.height) - (5*self.age)
        super(User, self).save(force_insert, force_update, using, update_fields) 



class Food(models.Model):
    Food_name = models.CharField(max_length=200)
    Description = models.TextField(default='-', blank=True)
    Food_price = models.DecimalField(default='-',max_digits=10, decimal_places=2)
    Image = models.ImageField(null=True,blank=True,upload_to='images/')
    Calories = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Food_name

class Cart(models.Model):
    Food_name = models.CharField(max_length=200)
    Description = models.TextField(default='-', blank=True)
    Food_price = models.DecimalField(default='-',max_digits=10, decimal_places=2)
    Image = models.ImageField(null=True,blank=True,upload_to='images/')
    Calories = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Food_name
