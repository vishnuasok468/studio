from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def d_login(request):
    return render(request,'login.html')

def login(request):
    messages.success(request,'Succefully Logged in!!!')
    return redirect('d_login')

def d_reg(request):
    return render(request,'reg.html')

def reg(request):
    messages.success(request,'Succefully signed up!!!')
    return redirect('d_reg')

def equip(request):
    return render (request,'equipments.html')

def booknow(request):
    messages.info(request,'Login Required!!')
    return redirect('home')