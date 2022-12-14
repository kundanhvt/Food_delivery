from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from reastaurant.models import Restaurant, Image, Food
from .models import users, Address
import logging
from core import settings
from django.views.decorators.csrf import csrf_exempt
import json
from reastaurant.models import Image



def home(request):
    restaurents = Restaurant.objects.all()
    foods = Food.objects.all()
    return render(request, "index.html",context= {"restaurants": restaurents, "foods":foods})

def custom_login(request):
    if request.method == 'POST':
        data = request.POST.dict()
        email=data.get('email')
        password=data.get('password')
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request, user)
            print('login successfull')
            print(request.user.username)
            return redirect('/')
        else:
            return render(request,'login.html',{
                    'error':True
            })

    return render(request,'login.html',{
        'error':False,
    })
def signup(request):
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            email=data.get('email')
            password=data.get('password')
            cpassword=data.get('cpassword')
            print(password)
            print(cpassword)
            if password != cpassword:
                return render(request,'signup.html',{"same_password":True} )
            user = users.objects.create_user(email=email, password=password)
            return redirect(reverse('user:login'))
        except Exception as ex :
            print('Exception occured')
            print(ex)
            return render(request, 'signup.html',{
                'error':True
            })

    return render(request, 'signup.html',{
        'error':False,
        "same_password":False
    })

def custom_logout(request):
    print(request.user)
    logout(request)
    print(request.user)
    print('logout successfully')
    return redirect('/')

def profile_update(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        file = request.FILES.get('file')
        user = users.objects.get(id=request.user.id)
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.phone = data['phone']
        if file is not None:
            user.image = file
        if user.address == None:
            print('address is not available')
            address = Address(area=data['area'],city=data['city'],state=data['state'],country=['country'], pincode=data['pincode'])
            address.save()
            user.address = address
        else:
            user.address.area = data['area']
            user.address.city = data['city']
            user.address.state = data['state']
            user.address.country = data['country']
            user.address.pincode = data['pincode']
            user.address.save()
        user.save()
        return HttpResponse('success!!')
    return render(request,'profile_update.html')

def profile(request):
    return render(request,'profile.html')