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
    menus = Menu.objects.filter(restaurant=rest_id)
    menu = Menu.objects.get(menu_type=menus.menu_type)
    print menu
    # print menu
    # context = {
    #     'items': items.menu.all(),
    #     'menu': Menu.objects.filter(menu_type=menu_type)
    # }
    return render(request, 'menus/show.html', context)
