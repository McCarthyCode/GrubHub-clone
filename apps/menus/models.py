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
        return (True, ["none"])

    def update_menu(self, postData):
        errors = []
        if len(postData['menu_name']) < 1:
            errors.append("Please enter a Menu Name")
            return (False, errors)
        menu = Menu.objects.get(id=postData['menu_id'])
        menu.menu_name = postData['menu_name']
        menu.save()
        return (True, ["none"])

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
