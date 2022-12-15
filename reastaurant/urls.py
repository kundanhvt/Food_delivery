from django.urls import path
from . import views
app_name = 'reastaurent'
urlpatterns = [
    path('/<id>',views.restaurant,name='restaurant'),
    path('all/',views.restaurants,name="restaurant_all"),
    path('cart/',views.cart, name='cart'),
    path('add_to_cart/<res_id>/<food_id>/',views.add_to_cart,name="add_to_cart"),
    path('increment_quantity/<cart_id>/',views.increment_quantity,name="increment_quantity"),
    path('decrement_quantity/<cart_id>/',views.decrement_quantity,name="decrement_quantity"),
    path('delete_all_cart/',views.delete_all_cart,name="delete_all_cart"),
    path('delete_cart/<cart_id>/',views.delete_cart,name="delete_cart"),
    path('food/<id>/',views.food,name='food'),
    path('view_all_food',views.view_all_food,name='view_all_food'),
    path('shipping',views.shipping,name="shipping")
]
