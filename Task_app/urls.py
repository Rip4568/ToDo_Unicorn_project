from django.urls import path
from .  import views

app_name = "Task_app"
#configurar as ações: deletar todas as tasks e adicionar 3 tasks aleatorias
urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='Home'),
    path('deletar_todas_as_tasks/',views.deletar_todas_as_tasks,name='deletar_todas_as_tasks'),
    
]