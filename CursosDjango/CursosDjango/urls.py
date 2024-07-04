"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as views_cursos
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PaginaPrincipal, name='Home'),
    path('cursos/', views_cursos.viewCursos, name='Cursos'),
    path('contacto/', views.contacto, name='Contacto'),
    path('formulario/', views.formulario, name='Formulario'),
    path('ejemplo/', views.ejemplo, name='Ejemplo'),
    #
    path('consultas1/', views_cursos.consultar1, name='Consultar1'),
    path('consultas2/', views_cursos.consultar2, name='Consultar2'),
    path('consultas3/', views_cursos.consultar3, name='Consultar3'),
    path('consultas4/', views_cursos.consultar4, name='Consultar4'),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)