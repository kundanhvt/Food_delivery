from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from reastaurant.models import Restaurant, Image, Food
from .models import users, Address
import logging
from django.views.decorators.csrf import csrf_exempt
import json
from reastaurant.models import Image
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim



def home(request):
    # print(request.session.get('latitude',None))
    restaurents = Restaurant.objects.all()[:10]
    foods = Food.objects.all()[:10]
    return render(request, "index.html",context= {"restaurants": restaurents, "foods":foods})

def custom_login(request):
    if request.method == 'POST':
        try:
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
        except Exception as ex:
            logging.warning(ex)
            return render(request,'error.html')

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

@login_required(login_url='user:login')
def custom_logout(request):
    logout(request)
    print('logout successfully')
    return redirect('/')

@login_required(login_url='user:login')
def profile_update(request):
    if request.method == 'POST':
        try:
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
                address = Address(area=data['area'],city=data['city'],state=data['state'],country=data['country'], pincode=data['pincode'])
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
        except Exception as ex:
            logging.warning(ex)
            return render(request,'error.html')
    return render(request,'profile_update.html')

@login_required(login_url='user:login')
def profile(request):
    return render(request,'profile.html')

def page404(request, exception):
    return render(request,'page404.html')

def update_session(request):
    data = request.POST.dict()
    print(data)
    request.session['latitude'] = data['latitude']
    request.session['longitude'] = data['longitude']

    geolocator = Nominatim(user_agent="kundan")
    latitude = request.session.get('latitude',None)
    longitude = request.session.get('longitude',None)
    location = geolocator.reverse(latitude+","+longitude)
    address = location.raw['address']
    city = None
    state = None
    restaurants = None
    foods = None
    if 'city' not in address.keys() and 'state' not in address.keys():
        restaurants = Restaurant.objects.all().order_by('id')
    elif 'city' not in address.keys():
        state = address['state']
        print('restaurant all')
        add = Address.objects.filter(state__iexact=state).values_list('id')
        restaurants = Restaurant.objects.filter(address__id__in=add).order_by('id')
    elif 'state' not in address.keys():
        city = address['city']
        print('restaurant all')
        add = Address.objects.filter(city__iexact=city).values_list('id')
        restaurants = Restaurant.objects.filter(address__id__in=add).order_by('id')
    else:
        city = address['city']
        state = address['state']
        print('restaurant all')
        add = Address.objects.filter(city__iexact=city,state__iexact=state).values_list('id')
        restaurants = Restaurant.objects.filter(address__id__in=add).order_by('id')
        foods = Food.objects.filter(restaurants_foods__id__in = restaurants.values_list('id'))[:10]        
    return render(request, "content.html",context= {"restaurants": restaurants, "foods":foods})
