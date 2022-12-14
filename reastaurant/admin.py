from django.contrib import admin
from .models import Category, Image, Food, Item, Restaurant, Cart

@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ['name','rating']

admin.site.register(Image)

@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['food']
