from django.urls import path, include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('inicio', views.inicio, name='inicioRedirect'),
    path('marca/', views.marca, name='marca'),
    path('categoria/', views.categoria, name='categoria'),
    path('producto/', views.producto, name='producto'),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
]

    


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)