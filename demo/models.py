# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'

    def get_name(self):
        return self.user.get_full_name()


class Admin(Usuario):
    def is_admin(self):
        return True


class PersonaNatural(Usuario):
    # CARGO = (
    #    ('0', 'Profesor'),
    #    ('1', 'Auxiliar'),
    #    ('2', 'Ayudante'),
    #    ('3', 'Estudiante'),
    # )
    # dicc = dict(CARGO)
    curso = models.ManyToManyField('Curso', through='Cargo')

    def is_admin(self):
        return False

    def cargo_persona(self):
        return self.cargo_set.order_by('-curso__anho','-curso__semestre','curso__seccion').first().cargo

    def coevaluaciones(self):
        return Coevaluacion.objects.filter(curso__in=self.curso.filter(cargo__cargo='3')).order_by('-fecha_inicio')

class Curso(models.Model):
    SEMESTRE = (
        ('0', 'Verano'),
        ('1', 'Otoño'),
        ('2', 'Primavera'),
    )
    integrantes = models.ManyToManyField('PersonaNatural', related_name='curso_integrantes', through='Cargo')
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    seccion = models.IntegerField()
    anho = models.IntegerField()
    semestre = models.CharField(
        max_length=1,
        choices=SEMESTRE,
    )

    def __str__(self):
        return f'{self.codigo}-{self.nombre}-{self.seccion}-{self.semestre}-{self.anho}'


class Cargo(models.Model):
    CARGO = (
        ('0', 'Profesor'),
        ('1', 'Auxiliar'),
        ('2', 'Ayudante'),
        ('3', 'Estudiante'),
    )
    persona = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    cargo = models.CharField(
        max_length=1,
        choices=CARGO
    )

    def __str__(self):
        return f'{self.persona}-{self.cargo}-{self.curso}'


class Equipo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    integrantes = models.ManyToManyField('PersonaNatural')

    def __str__(self):
        return f'{self.nombre}'


class Coevaluacion(models.Model):
    ESTADO = (
        ('0', 'Abierta'),
        ('1', 'Cerrada'),
        ('2', 'Publicada'),
    )
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=1,
        choices=ESTADO,
        default=0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    preguntas = models.OneToOneField('Preguntas', related_name='coevaluacion', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha_inicio}-{self.fecha_fin}'

    def instancia_coevaluacion(self,user):
        return self.instanciacoevaluacion_set.filter(evaluador=user)

    def pendiente(self, user):
        contestadas= self.instanciacoevaluacion_set.filter(evaluador=user).count()
        integrantes = user.equipo_set.filter(curso=self.curso).first().integrantes.count()
        return contestadas, integrantes

class InstanciaCoevaluacion(models.Model):
    evaluador = models.ForeignKey(PersonaNatural, related_name='instancia_coevaluacion_evaluador',
                                  on_delete=models.CASCADE)
    evaluado = models.ForeignKey(PersonaNatural, related_name='instancia_coevaluacion_evaluado',
                                 on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_coevaluacion = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE)
    fecha_respuesta = models.DateField(default=None)
    respuesta = models.OneToOneField('Respuesta', related_name='instancias_coevaluacion', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha_respuesta}'


class Preguntas(models.Model):
    p1 = models.CharField(max_length=1100)
    p2 = models.CharField(max_length=1100)
    p3 = models.CharField(max_length=1100)
    p4 = models.CharField(max_length=1100)
    p5 = models.CharField(max_length=1100)
    p6 = models.CharField(max_length=1100)
    p7 = models.CharField(max_length=1100)
    p8 = models.CharField(max_length=1100)
    p9 = models.CharField(max_length=1100)
    p10 = models.CharField(max_length=1100)

    def __str__(self):
        return f'{self.p1}'


class Respuesta(models.Model):
    NOTA = (
        ('0', '1.0'),
        ('1', '2.0'),
        ('2', '3.0'),
        ('3', '4.0'),
        ('4', '5.0'),
        ('5', '6.0'),
        ('6', '7.0'),
    )
    p1 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p2 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p3 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p4 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p5 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p6 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p7 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p8 = models.CharField(
        max_length=1,
        choices=NOTA
    )
    p9 = models.CharField(max_length=1100)
    p10 = models.CharField(max_length=1100)

    def __str__(self):
        return f'{self.p1}'
