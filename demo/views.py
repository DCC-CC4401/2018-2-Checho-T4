# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView


class DemoView(TemplateView):
    template_name = 'demo.html'
