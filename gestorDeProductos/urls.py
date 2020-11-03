from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('producto', views.producto, name='producto'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)