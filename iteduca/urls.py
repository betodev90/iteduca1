"""iteduca URL Configuration

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
from courses.views import index, lista_cursos
from estudiantes.views import registrar_estudiante, editar_estudiante, lista_estudiantes
from accounts.views import login_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/$', index, name='inicio'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),

    # cursos
    url(r'^cursos/$', lista_cursos, name='lista_cursos'),

    # estudiante
    url(r'^estudiantes/$', lista_estudiantes, name='lista_estudiantes'),
    url(r'^estudiantes/nuevo/$', registrar_estudiante, name='registrar_estudiante'),
    url(r'^estudiantes/editar/(?P<pk>\d+)/$', editar_estudiante, name='editar_estudiante')

]
