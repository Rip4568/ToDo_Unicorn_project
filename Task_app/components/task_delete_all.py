from django_unicorn.components import UnicornView
from Task_app.models import Task

class TaskDeleteAllView(UnicornView):
    
    def deletar(self):
        Task.objects.all().delete()
