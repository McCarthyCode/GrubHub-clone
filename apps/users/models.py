# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class Grubber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)

class GrubberManager(models.Manager):
    def login_reg_validator(self, postData, action):
        errors = []
        # checks if user is registering
        if action == 'register':
            if len(postData['username']) < 1:
                errors.append("Please put in a Username!")
            if len(postData['first_name']) < 1:
                errors.append("Please put in a first name!")
            if len(postData['last_name']) < 1:
                errors.append("Please put in a last name!")
            if len(postData['address_1']) < 1:
                errors.append("Please enter an address!")
            if len(postData['city']) < 1:
                errors.append("Please enter a city!")
            if len(postData['state']) < 1:
                errors.append("Please enter a state!")
            if len(postData['email']) < 1:
                errors.append("Please enter an email!")
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")
            if len(postData['password']) < 8:
                errors.append("Please enter a password!")
            if postData['conf_pw'] != postData['password']:
                errors.append("Password must match!!")
        elif action == 'login':
            if len(postData['email']) < 1:
                errors.append("Please enter your email!")
            elif not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")
    
        email_exists = User.objects.filter(email_address=postData['email'])

        if not errors:
            # checks if user is registering
            if action == 'register':
                if len(email_exists) != 0:
                    # checks if registering user email already exists
                    errors.append('This user exists!')
                    return (False, errors)
                #otherwise bcrypt password and create user
                user = User.objects.create_user(
                    username=postData['username'],
                    last_name=postData['last_name'],
                    email_address=postData['email'],
                    password=postData['password']
                )
                Grubber.objects.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    address_1=postData['address_1'],
                    address_2=postData['address_2'],
                    city=postData['city'],
                    state=postData['state'],
                    user=user
                )
                return (True, user)
            elif action == 'login':
                #compares user password with posted password
                correct_pw = User.check_password(postData['password'])
                if not correct_pw:
                    errors.append("This user either doesn't exist or the password is wrong... figure it out.")
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

#payment info model to be added as unique model - on to many relationship
