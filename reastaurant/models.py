from django.db import models
from user.models import Address

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
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True, related_name='food_items')

    def __str__(self):
        return self.name

class Reastaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name="reastaurant_image_name")
    address = models.ForeignKey(Address,on_delete=models.CASCADE, related_name="reastaurents_address")
    food = models.ManyToManyField(Food,null=True, blank=True ,related_name="reastaurants_foods")
    rating = models.IntegerField()

    def __str__(self):
        return self.name