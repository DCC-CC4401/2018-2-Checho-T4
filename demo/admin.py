# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from demo.models import PersonaNatural
from demo.models import Admin
from demo.models import Curso
from demo.models import Cargo
from demo.models import Equipo
from demo.models import Coevaluacion
from demo.models import InstanciaCoevaluacion
from demo.models import Respuesta

admin.site.register(PersonaNatural)
admin.site.register(Admin)
admin.site.register(Curso)
admin.site.register(Cargo)
admin.site.register(Equipo)
admin.site.register(Coevaluacion)
admin.site.register(InstanciaCoevaluacion)
admin.site.register(Respuesta)
