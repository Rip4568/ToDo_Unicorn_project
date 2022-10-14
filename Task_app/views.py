import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView,CreateView

from .models import Task
from .forms import TaskForm

TEMPLATE_NAME_INDEX = "Task_app/index.html"

class HomeTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm()
        context["tasks"] = Task.objects.all().reverse()
        return context
    
    template_name = TEMPLATE_NAME_INDEX

def deletar_todas_as_tasks(request):
    Task.objects.all().delete()
    return redirect(reverse("Task_app:Home"))

def adicionar_3_tasks_aleatorias(request):
    v = ['fazer','terminar','começar','concluir','mostar']
    a = ['o computador novo','o livro comprado recente','a cama','a arrumação do quarto']
    for i in range(3):
        new_task_random_titulo = "{} {}".format(random.choice(v),random.choice(a))
        Task.objects.create(titulo=new_task_random_titulo).save()
    return redirect(reverse("Task_app:Home"))