from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as login_fun, logout
from reastaurant.models import Reastaurant, Image
import logging
from core import settings


def home(request):
    restaurents = Reastaurant.objects.all()
    images = Image.objects.all()    
    return render(request, "index.html",context= {"restaurants": restaurents, "foods":"","images":images})

def login(request):
    if request.method == 'POST':
        data = request.POST.dict()
        username=data.get('username')
        password=data.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login_fun(request, user)
            print('login successfull')
            print(request.user.username)
            return redirect('/post/')
        else:
            return render(request,'login.html',{
                    'error':True
            })

    return render(request,'login.html',{
        'error':False
    })
def signup(request):
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            print(data)
            first=data.get('first')
            last=data.get('last')
            username=data.get('username')
            password=data.get('password')
            email=data.get('email')
            city=data.get('city')
            phone=data.get('phone')
            return redirect(reverse('user:login'))
        except Exception as ex :
            print('Exception occured')
            print(ex)
            return render(request, 'signup.html',{
                'error':True
            })

    return render(request, 'signup.html',{
        'error':False
    })
