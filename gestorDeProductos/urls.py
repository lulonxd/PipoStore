from django.urls import path, include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from gestorDeProductos.views import RegistroUsuario

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('producto', views.producto, name='producto'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', RegistroUsuario.as_view(), name='registro'),
    path('accounts', include('django.contrib.auth.urls')),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
]

    


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)