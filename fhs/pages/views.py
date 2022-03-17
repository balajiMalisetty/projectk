from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import *
from .models import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)


def food(request):

    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'pages/homepage.html', context)

def search_food(request):
    if request.method == "POST":
        searched = request.POST['searched']
        foods = Food.objects.filter(Food_name__contains=searched)
        return render(request,'pages/search.html',{'searched':searched,'foods':foods})

def profile(request):
    return render(request,'pages/profile.html')

def cart(request):
    
    cart1 = Cart.objects()
    cart1.food_name = cart_item.Food_name
    if car1.is_valid():
        cart1.save()
        messages.success(request, f'Item is added into cart')

        



    


