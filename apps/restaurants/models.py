# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ..users.models import Grubber
from datetime import datetime
# Create your models here.
class RestaurantManager(models.Manager):
    def create_restaurant(self, postData, categories):
    #pull in user info using hidden input??
        owner = User.objects.get(id=postData['user_id'])
        errors = []
        if len(postData['rest_name']) < 1:
            errors.append("Please enter a Restaurant Name")
        
        if not errors:
            new_r = Restaurant.objects.create(
                rest_name = postData['rest_name'],
                owned_by = owner,
            )
            for cat in categories:
                new_r.category.add(cat)
            all_restaurants = Restaurant.objects.filter(owned_by=owner.id)
            return (True, all_restaurants)
        return (False, errors)


class RestaurantAddressManager(models.Manager):
    def address_validator(self, postData):
        errors = []
        if len(postData['address_1']) < 1:
            errors.append("Please enter an address!")
        if len(postData['city']) < 1:
            errors.append("Please enter a city!")
        if len(postData['state']) < 1:
            errors.append("Please enter a state!")
        if len(postData['zip_code']) < 1:
            errors.append("Please enter a zip code!")
        if len(postData['phone_number']) < 1:
            errors.append("Please enter a phone number")

        address_exists = RestaurantAddress.objects.filter(
            address_1=postData['address_1'])

        if not errors:
            restaurant = Restaurant.objects.get(id=postData['rest_id'])
            if address_exists:
                errors.append("This address exists!")
            RestaurantAddress.objects.create(
                address_1=postData['address_1'],
                address_2=postData['address_2'],
                city=postData['city'],
                state=postData['state'],
                zip_code=postData['zip_code'],
                phone_number=postData['phone_number'],
                address_label=postData['address_label'],
                rest_addresses=restaurant,
                #to be pulled from hidden input in template
            )
            all_addresses = RestaurantAddress.objects.filter(rest_addresses_id=restaurant.id)
            return (True, all_addresses)

        return (False, errors)

# class MenuManager(models.Manager):

class Restaurant(models.Model):
    rest_name = models.CharField(max_length=255)
    rest_owner = models.ForeignKey(User, name="owned_by")
    #profile_photo
    #cover_photo
    category = models.ManyToManyField('RestaurantCategory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RestaurantManager()

class RestaurantAddress(models.Model):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    rest_addresses = models.ForeignKey(Restaurant, related_name='locations', null=True, blank=True)
    address_label = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RestaurantAddressManager()

class RestaurantCategory(models.Model):
    restaurant_categories = models.CharField(max_length=100)
    #category_img = 

class MenuItem(models.Model):
    menu_item = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, name="menu")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Menu class