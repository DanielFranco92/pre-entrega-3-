from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('profesores/', views.profesores, name="profesores"),
    path('cursos/', views.cursos, name="cursos"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('buscar/', views.buscar)
]