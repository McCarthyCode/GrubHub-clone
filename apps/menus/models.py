# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ..users.models import Grubber
from datetime import datetime
from ..restaurants.models import Restaurant
# Create your models here.

# class MenuManager(models.Manager):
#     def 



class Menu(models.Model):
    menu_type = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MenuItem(models.Model):
    item = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
