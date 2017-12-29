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

    def update_restaurant(self, postData, categories, value):
        rest_updating = Restaurant.objects.get(id=postData['rest_id'])
        errors = []
        if len(postData['rest_name']) < 1:
            errors.append("Please enter a Restaurant Name")
        if not errors:
            rest_updating.rest_name = postData['rest_name']
            rest_updating.save()
            if value == 'add':
                for cat in categories:
                    rest_updating.category.add(cat)
            if value == 'remove':
                for cat in categories:
                    rest_updating.category.remove(cat)
            rest_updating.save()
            return (True, rest_updating)
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

    def update_location(self, postData):
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

        address_updating = RestaurantAddress.objects.get(id=postData['location_id'])

        if not errors:
            address_updating.address_1 = postData['address_1']
            address_updating.address_2 = postData['address_2']
            address_updating.city = postData['city']
            address_updating.state = postData['state']
            address_updating.zip_code = postData['zip_code']
            address_updating.phone_number = postData['phone_number']
            address_updating.address_label = postData['address_label']
            address_updating.save()
            return (True, address_updating)
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