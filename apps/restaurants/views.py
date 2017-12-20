# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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
    # return HttpResponse('placeholder for restuarant profile')
    rest = Restaurant.objects.get(id=rest_id)
    request.session['rest_id'] = rest.id
    context = {
        'restaurant': rest,
        'locations': RestaurantAddress.objects.filter(rest_addresses_id=rest.id),
        'categories': rest.category.all(),
        'all_cats': RestaurantCategory.objects.all()
    }
    return render(request, 'restaurants/show.html', context)

def add_restaurant(request):
    categories = request.POST.getlist('category')
    Restaurant.objects.create_restaurant(request.POST, categories)
    return redirect('restaurants:restaurant_home')

def update_restaurant(request):
    categories = request.POST.getlist('category')
    rest_id = request.session['rest_id']
    value = request.POST['selector']
    valid, response = Restaurant.objects.update_restaurant(request.POST, categories, value)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('restaurants:rest_profile', rest_id)
    return redirect('restaurants:rest_profile', rest_id)

def destroy_restaurant(request):
    #need to delete address as well
    rest_id = request.session['rest_id']
    rest_deleting = Restaurant.objects.get(id=rest_id)
    rest_deleting.delete()
    return redirect('restaurants:restaurant_home')

def add_location(request):
    valid, response = RestaurantAddress.objects.address_validator(request.POST)
    rest_id = request.session['rest_id']
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('restaurants:rest_profile', rest_id)
    print response.values()
    return redirect('restaurants:rest_profile', rest_id)
