# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse

from django.views.generic import TemplateView
from .models import *


class LoginView(TemplateView):
    template_name = 'login.html'


def inicio_sesion(request):
    if request.POST:
        username = request.POST.get('rut')
        password = request.POST.get('password')
        log_user = authenticate(request, username=username, password=password)
        if log_user is not None:
            login(request, log_user)
            return HttpResponseRedirect('/home')
    logout(request)
    return render(request, 'login.html', {})


class Coevaluacion(TemplateView):
    pass


class CoevaluacionAlumnoView(TemplateView):
    template_name = 'coevaluacion-vista-alumno.html'


class CoevaluacionDocenteView(TemplateView):
    template_name = 'coevaluacion-vista-docente.html'


class Curso(TemplateView):
    pass


class CursoAlumnoView(TemplateView):
    template_name = 'curso-vista-alumno.html'


class CursoDocenteView(TemplateView):
    template_name = 'curso-vista-docente.html'


class Home(TemplateView):
    pass


def home(request):
    log_user = request.user
    try:
        user = User.objects.get(username=log_user)
        if (PersonaNatural.objects.filter(user=log_user)):
            persona = PersonaNatural.objects.filter(user=log_user).first()
            print(persona)
            cargo = persona.cargo_persona()
            if (cargo == '0'):  # profesor
                return render(request, 'home-vista-profesor.html', {})
            elif (cargo == '1' or cargo == '2'):  # auxiliar o ayudante
                return render(request, 'home-vista-docente.html', {})
            elif (cargo == '3'):  # alumno
                nombre = persona.get_name()
                cargos = persona.cargo_set.order_by('-curso__anho', '-curso__semestre', 'curso__seccion')
                ultimas_coevaluaciones_curso = persona.coevaluaciones()[0:9]
                return render(
                    request,
                    'home-vista-alumno.html',
                    {'user':persona,
                        'nombre': nombre,
                     'cargos': cargos,
                     'ultimas_coevaluaciones_curso': ultimas_coevaluaciones_curso,})
            else:
                return HttpResponseNotFound()
        elif (Admin.objects.filter(user=log_user)):
            return HttpResponseRedirect('admin')
        else:
            return HttpResponseNotFound('Debes estar registrado en el sistema como persona natural o administrador')
    except Exception as e:
        print(e)
        return HttpResponseNotFound()


class HomeAlumnoView(TemplateView):
    template_name = 'home-vista-alumno.html'


class HomeDocenteView(TemplateView):
    template_name = 'home-vista-docente.html'


class HomeProfesorView(TemplateView):
    template_name = 'home-vista-profesor.html'


class Perfil(TemplateView):
    pass


class PerfilDuenoView(TemplateView):
    template_name = 'perfil-vista-dueno.html'


class PerfilAlumnoDocenteView(TemplateView):
    template_name = 'perfil-alumno-vista-docente.html'
