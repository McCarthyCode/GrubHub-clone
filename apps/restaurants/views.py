# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, RestaurantAddress, RestaurantCategory
from ..users.models import User

# Create your views here.
def show_restaurants(request):
    owner = User.objects.get(id=request.session['id'])
    u_rest = Restaurant.objects.filter(owned_by=owner)
    # r_cat = RestaurantCategory.objects.filter(restaurant_id=u_rest)
    categories = RestaurantCategory.objects.all()
    context = {
        'restaurants': u_rest,
        # 'locations': locations,
        'categories': categories,
        'user': owner
    }
    return render(request, 'restaurants/index.html', context)

def rest_profile(request, rest_id):
    print "all good"
    return HttpResponse('placeholder for restuarant profile')
    # rest = Restaurant.objects.get(rest_name=rest_id)
    # context = {
    #     'restaurant': rest,
    # }
    # return render(request, 'restaurants/show.html', context)

def add_restaurant(request):
    categories = request.POST.getlist('category')
    Restaurant.objects.create_restaurant(request.POST, categories)
    return redirect('restaurants:restaurant_home')
