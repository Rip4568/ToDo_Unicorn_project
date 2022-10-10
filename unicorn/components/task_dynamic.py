from django import forms
from django_unicorn.components import UnicornView, QuerySetType
from Task_app.models import Task

from Task_app.forms import TaskForm

""" class ValidationForm(forms.Form):
    task = forms.CharField(max_length=10,min_length=2)
 """
class TaskDynamicView(UnicornView):
    form_class = TaskForm
    tasks: QuerySetType[Task] = Task.objects.all()
    task: str = ""
    
    
    """ context["form"] = TaskForm() """
    def atualizar_tasks(self):
        self.tasks = Task.objects.all().reverse()

    def salvar_task(self):#metodo para salvar, necessario chamar no html
        if self.is_valid():#se o metodo de input atual (self) for valido
            Task.objects.create(titulo=self.task)#criação e salvamento da nova task
            self.atualizar_tasks()
            self.task = "" #limpar o input
    
    def deletar_todas_as_tasks(self):
        Task.objects.all().delete()
        self.tasks = Task.objects.none()
        
    def deletar_task(self,task_id):
        Task.objects.get(id=task_id).delete()
        self.atualizar_tasks()
