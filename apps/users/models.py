# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class GrubberManager(models.Manager):
    def login_reg_validator(self, postData, action):
        errors = []
        # checks if user is registering
        if action == 'register':
            if len(postData['first_name']) < 1:
                errors.append("Please put in a first name!")
            if len(postData['last_name']) < 1:
                errors.append("Please put in a last name!")
            if len(postData['email']) < 1:
                errors.append("Please enter an email!")
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")
            if len(postData['password']) < 8:
                errors.append("Please enter a password!")
            if postData['confirm_password'] != postData['password']:
                errors.append("Password must match!!")
        elif action == 'login':
            if len(postData['email']) < 1:
                errors.append("Please enter your email!")
            elif not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")

        email_exists = User.objects.filter(email=postData['email'])

        if not errors:
            # checks if user is registering
            if action == 'register':
                if len(email_exists) != 0:
                    # checks if registering user email already exists
                    errors.append('This user exists!')
                    return (False, errors)
                #otherwise bcrypt password and create user
                user = User.objects.create_user(
                    username=postData['email'],
                    email=postData['email'],
                    password=postData['password']
                )
                user.first_name = postData['first_name']
                user.last_name = postData['last_name']
                user.save()
                return (True, user.id)
            elif action == 'login':
                #compares user password with posted password
                correct_pw = email_exists[0].check_password(
                    postData['password']) if len(email_exists) > 0 else False
                if not correct_pw:
                    errors.append(
                        "This user either doesn't exist or the password is wrong... figure it out.")
                    return (False, errors)
                #checks if user logging in exists
                if len(email_exists) == 0:
                    #validates whether user actually exists
                    errors.append(
                        "This user either doesn't exist or the password is wrong... figure it out.")
                    return (False, errors)
                #grabs user id to store in session in views
                if correct_pw:
                    user_id = email_exists[0].id
                    return (True, user_id)
        return (False, errors)

    def modify_user(self, postData, action):
        user_updating = User.objects.get(id=postData['user_id'])
        correct_pw = user_updating.check_password(postData['current_password'])
        errors = []

        if len(postData['current_password']) < 1:
            errors.append("Please enter your password!")

        if not errors:
            if action == 'update_name':
                if len(postData['first_name']) < 1:
                    errors.append("Please put in a first name!")
                if len(postData['last_name']) < 1:
                    errors.append("Please put in a last name!")
                if not correct_pw:
                    errors.append("Please enter a password!")
                if not errors:
                    user_updating.first_name = postData['first_name']
                    user_updating.last_name = postData['last_name']
                    user_updating.save()
                    return (True, user_updating)
                return (False, errors)
            elif action == 'update_email':
                if len(postData['new_email']) < 1:
                    errors.append("Please enter an email!")
                if len(postData['conf_email']) < 1:
                    errors.append("Please enter an email")
                if not EMAIL_REGEX.match(postData['new_email']):
                    errors.append("Please enter a valid email!")
                if not EMAIL_REGEX.match(postData['conf_email']):
                    errors.append("Please enter a valid email!")
                if not correct_pw:
                    errors.append("Please enter a password!")
                if not errors:
                    user_updating.email = postData['new_email']
                    user_updating.save()
                    return (True, user_updating)
            elif action == 'update_password':
                if len(postData['new_password']) < 1:
                    errors.append("Please enter a password!")
                if len(postData['confirm_password']) < 1:
                    errors.append("Please enter a password!")
                if not correct_pw:
                    errors.append("Please enter a password!")
                if not errors:
                    user_updating.set_password(postData['new_password'])
                    user_updating.save()
                    return (True, user_updating)
                return (False, errors)
        return (False, errors)


class Grubber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_rest_owner = models.BooleanField(default=False, blank=True)
    objects = GrubberManager()

class AddressManager(models.Manager):
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

        address_exists = UserAddress.objects.filter(address_1=postData['address_1'])

        if not errors:
            user = User.objects.get(id=postData['user_id'])
            if len(address_exists) == 0:
                errors.append("This address exists!")
            UserAddress.objects.create(
                address_1=postData['address_1'],
                address_2=postData['address_2'],
                city=postData['city'],
                state=postData['state'],
                zip_code=postData['zip_code'],
                phone_number=postData['phone_number'],
                cross_street=postData['cross_street'],
                delivery_instructions=postData['delivery_instructions'],
                address_label=postData['address_label'],
                users_addresses=user,
                #to be pulled from hidden input in template
            )
            all_addresses = UserAddress.objects.filter(id=user.id)
            return (True, all_addresses)

        return (False, errors)

    def updated_address(self, postData):
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

        address_updating = UserAddress.objects.get(id=postData['address_id'])

        if not errors:
            address_updating.address_1 = postData['address_1']
            address_updating.address_2 = postData['address_2']
            address_updating.city = postData['city']
            address_updating.state = postData['state']
            address_updating.zip_code = postData['zip_code']
            address_updating.phone_number = postData['phone_number']
            address_updating.cross_street = postData['cross_street']
            address_updating.delivery_instructions = postData['delivery_instructions']
            address_updating.address_label = postData['address_label']
            address_updating.save()
            return (True, address_updating)
        return (False, errors)

class UserAddress(models.Model):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    cross_street = models.CharField(max_length=255, null=True, blank=True)
    delivery_instructions = models.CharField(max_length=255, null=True, blank=True)
    users_addresses = models.ForeignKey(User, related_name='addresses')
    address_label = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressManager()

#payment info model to be added as unique model - on to many relationship
