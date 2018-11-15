# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from demo.models import PersonaNatural
from demo.models import Admin

admin.site.register(PersonaNatural)
admin.site.register(Admin)