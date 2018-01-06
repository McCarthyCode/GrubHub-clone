# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ..users.models import Grubber
from datetime import datetime
from ..restaurants.models import Restaurant

class MenuManager(models.Manager):
    def create_menu(self, postData, rest_id):
        errors = []
        if len(postData['menu_name']) < 1:
            errors.append("Please enter a Menu Name")
            return (False, errors)
        Menu.objects.create(
            menu_name=postData['menu_name'],
            restaurant=Restaurant.objects.get(id=rest_id)
        )
        return (True, errors)

    def update_menu(self, postData):
        errors = []
        if len(postData['menu_name']) < 1:
            errors.append("Please enter a Menu Name")
            return (False, errors)
        menu = Menu.objects.get(id=postData['menu_id'])
        menu.menu_name = postData['menu_name']
        menu.save()
        return (True, errors)

    def destroy_menu(self, menu_id):
        errors = []
        menu = Menu.objects.get(id=menu_id)
        if not menu:
            errors.append("Invalid menu ID")
            return (False, errors)
        menu.delete()
        return (True, errors)

class MenuItemManager(models.Manager):
    def create_item(self, postData):
        errors = []
        errors_exist = False
        if len(postData['item']) < 1:
            errors.append("Please enter an Item Name")
            errors_exist = True
        if len(postData['price']) < 1:
            errors.append("Please enter a Price")
            errors_exist = True
        MenuItem.objects.create(
            item=postData['item'],
            desc=postData['desc'],
            price=postData['price'],
            menu=Menu.objects.get(id=postData['menu_id']),
        )
        if errors_exist:
            return (False, errors)
        return (True, errors)

class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MenuManager()

class MenuItem(models.Model):
    item = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MenuItemManager()
