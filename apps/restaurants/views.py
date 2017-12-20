# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, RestaurantAddress

# Create your views here.
def show_restaurants(request):
    locations = RestaurantAddress.objects.all()
    #need to call instance of restaurant to show locations - r.locations.all()
    context = {
        'restaurants': Restaurant.objects.all(),
        'locations': locations
    }
    return render(request, 'restaurants/index.html', context)
