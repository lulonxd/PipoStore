from django.urls import path
from . import views

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('producto', views.producto, name='producto'),
]