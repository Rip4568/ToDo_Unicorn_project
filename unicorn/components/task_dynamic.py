from django_unicorn.components import UnicornView
from Task_app.forms import TaskForm
from Task_app.models import Task
class TaskDynamicView(UnicornView):
    tasks:list=[]
    task:str=""
    
    def salvar_task(self):#metodo para salvar, necessario chamar no html
        if self.is_valid():#se o metodo de input atual (self) for valido
            Task.objects.create(titulo=self.task).save()#criação e salvamento da nova task
            self.tasks.append(self.task) #adicionar a lista para renderizar
            self.tasks.reverse()#sem esse metodo a lista fica desorganizada entre o for do index e o componente
            self.task = ""#limpar o input
