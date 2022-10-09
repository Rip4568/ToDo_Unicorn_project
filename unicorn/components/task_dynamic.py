from django.http import QueryDict
from django_unicorn.components import UnicornView, QuerySetType
from Task_app.models import Task

class TaskDynamicView(UnicornView):
    tasks: QuerySetType[Task] = Task.objects.all()
    task: str = ""
    
    def atualizar_tasks(self):
        self.tasks = Task.objects.all().reverse()

    def salvar_task(self):#metodo para salvar, necessario chamar no html
        if self.is_valid():#se o metodo de input atual (self) for valido
            Task.objects.create(titulo=self.task)#criação e salvamento da nova task
            """ self.tasks = Task.objects.all() #adicionar a lista para renderizar
            self.tasks.reverse()#sem esse metodo a lista fica desorganizada entre o for do index e o componente """
            self.atualizar_tasks()
            self.task = "" #limpar o input
    
    def deletar_todas_as_tasks(self):
        Task.objects.all().delete()
        self.tasks = Task.objects.none()
        
    def deletar_task(self,task_id):
        Task.objects.get(id=task_id).delete()
        self.atualizar_tasks()
        """ self.tasks = Task.objects.all() """