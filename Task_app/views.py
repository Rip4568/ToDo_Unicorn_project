from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView,CreateView
from .models import Task
from .forms import TaskForm

TEMPLATE_NAME_INDEX = "Task_app/index.html"

class HomeTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm
        context["tasks"] = Task.objects.all().order_by('-criado_em')
        return context
    
    template_name = TEMPLATE_NAME_INDEX
