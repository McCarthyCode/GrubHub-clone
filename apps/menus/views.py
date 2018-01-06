# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from ..users.models import User
from ..menus.models import Menu, MenuItem
from ..restaurants.models import Restaurant, RestaurantAddress, RestaurantCategory
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
# def convert_m_type(request, menu_type, rest_id):
#     l_menu_type = menu_type.lower()
#     print l_menu_type
#     return redirect('menus:menu_home', l_menu_type, rest_id)

def create_menu(request, rest_id):
    valid, response = Menu.objects.create_menu(request.POST, rest_id)
    if not valid:
        for error in response:
            messages.error(request, error)
    return redirect('restaurants:rest_profile', rest_id)

def update_menu(request, rest_id):
    valid, response = Menu.objects.update_menu(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
    return redirect('restaurants:rest_profile', rest_id)

def destroy_menu(request, rest_id, menu_id):
    valid, response = Menu.objects.destroy_menu(menu_id)
    if not valid:
        for error in response:
            messages.error(request, error)
    return redirect('restaurants:rest_profile', rest_id)

def menu_profile(request, rest_id):
    menus = Menu.objects.filter(
        restaurant_id=Restaurant.objects.get(rest_id)
    )
    context = {
        'menus': menus,
        'items': MenuItem.objects.filter(rest_id=menus.restaurant.id),
    }
    return render(request, 'menus/show.html', context)

# def create_menu(request, rest_id):
