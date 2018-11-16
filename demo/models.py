# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

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

class Coevaluacion(models.Model):
    fecha_inicio = models.DateField(default= date.today)
    fecha_fin = models.DateField()
    estado = models.CharField(default= 'Abierto')
    #curso = models.ForeignKey()

    def __str__(self):
        return f'{self.fecha_inicio}-{self.fecha_fin}'

class InstanciaCoevaluacion(models.Model):
    # evaluador = models.ForeignKey()
    # evaluado = models.ForeignKey()
    # grupo = models.ForeignKey()
    # id_coevaluacion = models.ForeignKey(Coevaluacion.indexes)
    fecha_respuesta = models.DateField(default= None)
    respondida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fecha_respuesta}'

class Respuesta(models.Model):
    # id_instancia = models.ForeignKey(InstanciaCoevaluacion.indexes)
    p1 = models.IntegerField(min_value 0, max_value=5)
    p2 = models.IntegerField(min_value=0, max_value=5)
    p3 = models.IntegerField(min_value=0, max_value=5)
    p4 = models.IntegerField(min_value=0, max_value=5)
    p5 = models.IntegerField(min_value=0, max_value=5)
    p6 = models.IntegerField(min_value=0, max_value=5)
    p7 = models.IntegerField(min_value=0, max_value=5)
    p8 = models.IntegerField(min_value=0, max_value=5)
    p9 = models.CharField()
    p10 = models.CharField()

    def __str__(self):
        return f'{self.indexes}'

