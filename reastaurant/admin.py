from django.contrib import admin
from .models import Category, Image, Food, Item, Reastaurant

@admin.register(Reastaurant)
class AdminReastaurant(admin.ModelAdmin):
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
