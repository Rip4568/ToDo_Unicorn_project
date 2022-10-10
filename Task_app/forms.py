from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(required=True, max_length=20,min_length=2,label="",strip=True)


""" class TaskForm(forms.ModelForm):
    #Colcoar widget para ter as mesmas configurações do formulario acima
    class Meta:
        model = Task
        fields = ("titulo",) """