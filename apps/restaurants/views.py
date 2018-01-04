# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..users.models import User
from ..menus.models import Menu, MenuItem
from .models import Restaurant, RestaurantAddress, RestaurantCategory


# Create your views here.
def show_restaurants(request):
    owner = User.objects.get(id=request.session['id'])
    u_rest = Restaurant.objects.filter(owned_by=owner)
    categories = RestaurantCategory.objects.all()
    context = {
        'restaurants': u_rest,
        'categories': categories,
        'user': owner
    }
    return render(request, 'restaurants/index.html', context)

def rest_profile(request, rest_id):
    rest = Restaurant.objects.get(id=rest_id)
    request.session['rest_id'] = rest.id
    context = {
        'all_cats': RestaurantCategory.objects.all(),
        'categories': rest.category.all(),
        'locations': RestaurantAddress.objects.filter(rest_addresses_id=rest.id),
        'menus': Menu.objects.filter(restaurant_id=rest.id),
        'restaurant': rest,
    }
    print rest.owned_by.id
    return render(request, 'restaurants/show.html', context)

def upload_profile_pic(request):
    rest_id = request.session['rest_id']
    profile_photo = request.FILES['myfile']
    valid, response = Restaurant.objects.upload_profile_photo(request.POST, profile_photo)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('restaurants:rest_profile', rest_id)
    return redirect('restaurants:rest_profile', rest_id)

def add_restaurant(request):
    categories = request.POST.getlist('category')
    Restaurant.objects.create_restaurant(request.POST, categories)
    return redirect('restaurants:restaurant_home')

def update_restaurant(request):
    categories = request.POST.getlist('category')
    rest_id = request.session['rest_id']
    valid, response = Restaurant.objects.update_restaurant(request.POST, categories)
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

def update_location(request):
    rest_id = request.session['rest_id']
    valid, response = RestaurantAddress.objects.update_location(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('restaurants:rest_profile', rest_id)
    return redirect('restaurants:rest_profile', rest_id)

def destroy_location(request, rest_id):
    #need to delete address as well
    location_deleting = Restaurant.location.get(id=rest_id)
    location_deleting.delete()
    return redirect('restaurants:restaurant_home')
