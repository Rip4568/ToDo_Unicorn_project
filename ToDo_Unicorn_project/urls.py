from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #rotas para sessão de admin
    path('admin/', admin.site.urls),
    #rotas para os aplicativos internos
    path('',include('Task_app.urls')),
    #rotas para as dependencias
    path('unicorn/',include('django_unicorn.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)