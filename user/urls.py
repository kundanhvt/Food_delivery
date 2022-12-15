from django.urls import path
from . import views


app_name= 'user'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.custom_login,name='login'),
    path('signup/',views.signup,name='signup'),   
    path('logout/',views.custom_logout,name='logout'),   
    path('profile_update/',views.profile_update,name='profile_update'),
    path('profile/',views.profile,name='profile'),
]



    

