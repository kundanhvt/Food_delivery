from django.shortcuts import render, redirect, reverse
from .models import Restaurant, Image, Food, Cart
from user.models import users
import logging
from django.core.paginator import Paginator

def restaurant(request, id):
    print(id)
    restaurent = Restaurant.objects.get(id=id)
    
    return render(request, "restaurant.html",context= {"restaurant": restaurent, "foods":""})

def restaurants(request):
    restaurants = Restaurant.objects.all().order_by('id')
    paginator = Paginator(restaurants, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'restaurants.html',context={"page_obj":page_obj})

def cart(request):
    carts = request.user.all_cart_food.all()
    total=0
    for cart in carts:
        total += cart.quantity * cart.food.price
    return render(request, "cart.html", context={"carts":carts,"total_price":total})

def add_to_cart(request, res_id, food_id):
    carts = request.user.all_cart_food.all()
    if(len(carts)==0):
        restaurant = Restaurant.objects.get(id=res_id)
        food = Food.objects.get(id=food_id)
        cart = Cart(food=food, quantity = 1,user=request.user, restaurant = restaurant)
        cart.save()
    else:
        res = carts[0].restaurant.id
        if int(res) != int(res_id):
            carts = request.user.all_cart_food.all()
            total=0
            for cart in carts:
                total += cart.quantity * cart.food.price
            return render(request, "cart.html", context={"carts":carts,"total_price":total,"cart_is_full":True})
        else:
            for cart in carts:
                if int(cart.food.id) == int(food_id):
                    cart.quantity = cart.quantity+1
                    cart.save()
                    return redirect(reverse('reastaurent:cart'))
            food = Food.objects.get(id=food_id)
            cart = Cart(food=food,quantity=1,user = request.user, restaurant =carts[0].restaurant)
            cart.save()
            print(cart)
    return redirect(reverse('reastaurent:cart'))


def decrement_quantity(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    if cart.quantity == 1:
        pass
    else:
        cart.quantity -=1
        cart.save()
    return redirect(reverse('reastaurent:cart'))

def increment_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.quantity +=1
    cart.save()
    return redirect(reverse('reastaurent:cart'))

def delete_cart(request,cart_id):
    cart = Cart.objects.get(id = cart_id)
    cart.delete()
    return redirect(reverse('reastaurent:cart'))

def delete_all_cart(request):
    carts = request.user.all_cart_food.all()
    for cart in carts:
        cart.delete()
    return redirect(reverse('reastaurent:restaurant_all'))