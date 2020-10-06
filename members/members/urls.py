"""members URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from memberarea import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aula/<int:a_id>', views.aula, name='aula'),
    path('aula/add', views.add_aula, name='add_aula'),
    path('aula/<int:a_id>/edit', views.edit_aula, name='edit_aula'),
    path('aula/<int:a_id>/del', views.del_aula, name='del_aula'),
    path('curso/<int:c_id>', views.curso, name='curso'),
    path('curso/add', views.add_curso, name='add_curso'),
    path('curso/<int:c_id>/edit', views.edit_curso, name='edit_curso'),
    path('cursos/', views.cursos, name='cursos'),
    path('curso/<int:c_id>/del', views.del_curso, name='del_curso'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
