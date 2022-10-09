from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #rotas para sessão de admin
    path('admin/', admin.site.urls),
    #rotas para os aplicativos internos
    path('',include('Task_app.urls')),
    #rotas para as dependencias
    path('unicorn/',include('django_unicorn.urls')),
]