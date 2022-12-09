from django.shortcuts import render
from .models import Reastaurant, Image
import logging

# Create your views here.

def home(request):
    restaurents = Reastaurant.objects.all()
    images = Image.objects.all()
    for img in images:
        logging.info(img)
    return render(request, "index.html",context= {"restaurants": restaurents, "foods":""})
