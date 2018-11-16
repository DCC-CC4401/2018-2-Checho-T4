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
    return '{self.email}-{self.rut}'

class Admin(Usuario):
  def is_admin(self):
    return True

class PersonaNatural(Usuario):
    curso = models.ManyToManyField('Curso', through='Cargo')
    def is_admin(self):
        return False

class Curso(models.Model):
    SEMESTRE = (
        (0, 'Verano'),
        (1, 'Otoño'),
        (2, 'Primavera'),
    )
    integrantes = models.ManyToManyField('PersonaNatural',related_name='curso_integrantes', through='Cargo')
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    seccion = models.IntegerField()
    anho = models.DateField()
    semestre = models.CharField(
        max_length=1,
        choices=SEMESTRE,
    )

class Cargo(models.Model):
    CARGO = (
        (0, 'Profesor'),
        (1, 'Auxiliar'),
        (2, 'Ayudante'),
        (3, 'Estudiante'),
    )
    estudiante = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    cargo = models.CharField(
        max_length=1,
        choices=CARGO
    )

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    integrantes = models.ManyToManyField('PersonaNatural', through='EstudianteEquipo')

class EstudianteEquipo(models.Model):
    estudiante = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

class Coevaluacion(models.Model):
    fecha_inicio = models.DateField(default= date.today)
    fecha_fin = models.DateField()
    #estado = models.CharField(default= 'Abierto')
    #curso = models.ForeignKey()

    def __str__(self):
        return '{self.fecha_inicio}-{self.fecha_fin}'

class InstanciaCoevaluacion(models.Model):
    evaluador = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    evaluado = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    # id_coevaluacion = models.ForeignKey(Coevaluacion.indexes)
    fecha_respuesta = models.DateField(default= None)
    respondida = models.BooleanField(default=False)

    def __str__(self):
        return '{self.fecha_respuesta}'

class Respuesta(models.Model):
    instancia_coevaluacion = models.ForeignKey(InstanciaCoevaluacion, on_delete=models.CASCADE)
    #p1 = models.IntegerField(min_value=0, max_value=5)
    #p2 = models.IntegerField(min_value=0, max_value=5)
    #p3 = models.IntegerField(min_value=0, max_value=5)
    #p4 = models.IntegerField(min_value=0, max_value=5)
    #p5 = models.IntegerField(min_value=0, max_value=5)
    #p6 = models.IntegerField(min_value=0, max_value=5)
    #p7 = models.IntegerField(min_value=0, max_value=5)
    #p8 = models.IntegerField(min_value=0, max_value=5)
    #p9 = models.CharField()
    #p10 = models.CharField()

    def __str__(self):
        return '{self.indexes}'

