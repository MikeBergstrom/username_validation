# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User

def index(request):
    print "in index"
    return render(request, 'validation/index.html')

def process(request):
    print "in process view"
    request.session['username'] = request.POST['username']
    user = User.objects.login(request.POST['username'])
    print user
    if 'errors' in user:
        print "if statement working"
        request.session['errors']=user['errors']
        print user['errors'][0]
        return redirect ('/')
    elif 'user' in user:
        request.session['errors'] = None
        print "in success"
        print user
        User.objects.create(username=request.POST['username'])
        usernames = User.objects.all()
        context = {"usernames":usernames}
        return render(request, 'validation/success.html', context)

# Create your views here.
