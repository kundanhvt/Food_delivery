from django.db import models
from user.models import Address
from user.models import users
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to="img")
    def __str__(self):
        return self.image.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='food_categories')

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ManyToManyField(Image)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='food_items')
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ManyToManyField(Image, related_name="restaurant_image_name")
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL, related_name="restaurant_address")
    phone = models.CharField(max_length=10,blank=True)
    food = models.ManyToManyField(Food,related_name="restaurants_foods")
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(users, on_delete=models.CASCADE, null=True,blank=True, related_name="all_cart_food")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)

class Order(models.Model):
    price = models.IntegerField(default=0)
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name="all_order_user")
    payment = models.CharField(max_length=20)