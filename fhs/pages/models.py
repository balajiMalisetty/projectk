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
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.id




class Diet(models.Model):
    Food_name = models.CharField(max_length=200)
    Description = models.TextField( blank=True)
    Food_price = models.IntegerField(default=0,null=True,blank=True)
    Breakfast = models.CharField(max_length=200)
    Image = models.ImageField(null=True,blank=True,upload_to='images/')
    price = models.IntegerField(default=0,null=True,blank=True)
    calories = models.IntegerField(default=0,null=True,blank=True)
    Lunch = models.CharField(max_length=200)
    Image1 = models.ImageField(null=True,blank=True,upload_to='images/')
    price1 = models.IntegerField(default=0,null=True,blank=True)
    calories1 = models.IntegerField(default=0,null=True,blank=True)
    Snack = models.CharField(max_length=200)
    Image2 = models.ImageField(null=True,blank=True,upload_to='images/')
    price2 = models.IntegerField(default=0,null=True,blank=True)
    calories2 = models.IntegerField(default=0,null=True,blank=True)
    Dinner = models.CharField(max_length=200)
    Image3 = models.ImageField(null=True,blank=True,upload_to='images/')
    price3 = models.IntegerField(default=0,null=True,blank=True)
    calories3 = models.IntegerField(default=0,null=True,blank=True)
    TCalories = models.IntegerField(default=0,null=True,blank=True)
    Tprice = models.IntegerField(default=0,null=True,blank=True)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.TCalories = self.calories + self.calories1 +self.calories2 + self.calories3
        self.Tprice = self.price + self.price1 +self.price2 + self.price3
        super(Diet, self).save(force_insert, force_update, using, update_fields) 

    def __str__(self):
        return self.Diet_name



class CartItem(models.Model):
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.item.Food_price * self.quantity

    def __str__(self):
        return self.product


class CartItemDiet(models.Model):
    item = models.ForeignKey(Diet, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def sub_total(self):
        return self.item.Food_price * self.quantity

    def __str__(self):
        return self.product