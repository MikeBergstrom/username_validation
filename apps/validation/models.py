# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class UserManager(models.Manager):
      def login(self, username):
          print "Running a login function!"
          if len(username) < 8:
              print "less than 8"
              return {'errors':['Username must be at least 8 characters']}
          elif len(username) > 26:
              print "over 26"
              return{'errors': ['Username ']}
          elif User.objects.filter(username=username).exists():
              return{'errors':['Username already in database']}
          else:
                print "login successful"
                return{'user': username}


class User(models.Model):
    username = models.CharField(max_length=26)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


# Create your models here.
