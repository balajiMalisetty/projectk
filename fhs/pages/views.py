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
    return render(request, 'pages/home.html', context)

def search_food(request):
    if request.method == "POST":
        searched = request.POST['searched']
        foods = Food.objects.filter(Food_name__contains=searched)
        return render(request,'pages/home.html',{'searched':searched,'foods':foods})


