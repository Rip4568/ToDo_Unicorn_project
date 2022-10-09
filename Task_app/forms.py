from django import forms
from .models import Task

class TaskForm(forms.Form):
    titulo = forms.CharField(required=True, max_length=20,min_length=2,label="",strip=True)


""" class TaskForm(forms.ModelForm):
    #Colcoar widget para ter as mesmas configurações do formulario acima
    class Meta:
        model = Task
        fields = ("titulo",) """