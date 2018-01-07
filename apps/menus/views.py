# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from ..users.models import User
from ..menus.models import Menu, MenuItem
from ..restaurants.models import Restaurant, RestaurantAddress, RestaurantCategory
from django.shortcuts import render, HttpResponse, redirect

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

def create_item(request, rest_id):
    valid, response = MenuItem.objects.create_item(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
    return redirect('restaurants:rest_profile', rest_id)

def update_item(request, rest_id):
    valid, response = MenuItem.objects.update_item(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
    return redirect('restaurants:rest_profile', rest_id)
