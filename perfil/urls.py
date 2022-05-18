from django.contrib import admin
from django.urls import path

from perfil_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('entrar/', views.entrar, name='entrar'),
]
