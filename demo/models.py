# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rut = models.IntegerField()
  email = models.EmailField()

  def __str__(self):
    return f'{self.email}-{self.rut}'

class PersonaNatural(Usuario):
  def is_admin(self):
    return False

class Admin(Usuario):
  def is_admin(self):
    return True
