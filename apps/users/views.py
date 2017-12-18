# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Grubber, GrubberManager

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
            messages.error(request.error)
        return redirect('users:index')
    return redirect("users:profile")

def profile(request):
    return HttpResponse('Placholder: Profile Page')

def reset(request):
    request.session.clear()
    return redirect('users:index')
