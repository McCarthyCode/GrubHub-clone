# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Grubber, GrubberManager, UserAddress

def index(request):
    return render(request, 'users/index.html')

def login(request):
    gm = GrubberManager()
    valid, response = gm.login_reg_validator(request.POST, 'login')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:index')
    request.session['id'] = response
    print response
    print "S'all good mang"
    return redirect("users:profile")

def register(request):
    gm = GrubberManager()
    valid, response = gm.login_reg_validator(request.POST, 'register')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:index')
    return redirect("users:profile")

def show_profile(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, "users/lets-eat.html", context)

def show_account(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, "users/account.html", context)

def show_addresses(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'addresses': user.addresses.all()
    }
    return render(request, "users/addresses.html", context)

def add_address(request):
    valid, response = UserAddress.objects.address_validator(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:user_addresses')
    return redirect('users:user_addresses')

def destroy_address(request, address_id):
    address_deleting = UserAddress.objects.get(id=address_id)
    address_deleting.delete()
    return redirect('users:user_addresses')

def update_address(request):
    response = UserAddress.objects.updated_address(request.POST)
    print response
    return redirect('users:user_addresses')

def reset(request):
    request.session.clear()
    return redirect('users:index')
