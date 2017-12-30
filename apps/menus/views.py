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

def menu_profile(request, menu_type, rest_id):
    menu = Menu.objects.filter(
        restaurant_id=rest_id
    ).get(menu_type=menu_type)
    context = {
        'menu': menu.menu_type.title(),
        'items': MenuItem.objects.filter(menu_id=menu.id),
    }
    print menu.menu_type
    return render(request, 'menus/show.html', context)

# def create_menu(request, rest_id):
