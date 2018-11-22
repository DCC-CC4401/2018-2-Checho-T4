"""coevaluaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import demo.views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^curso', demo.views.Curso.as_view()),
    url(r'^home', demo.views.Home.as_view(), name='home'),
    url(r'^coevaluacion', demo.views.Coevaluacion.as_view(), name='coevaluacion'),
    url(r'^perfil', demo.views.Perfil.as_view(), name='perfil'),
    url(r'^login', demo.views.inicio_sesion),
    url(r'', demo.views.LoginView.as_view(), name='login'),
]
