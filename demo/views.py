# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView



class LoginView(TemplateView):
    template_name = 'login.html'

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



