from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripciond e la tarea", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    title = forms.CharField(label="titulo del proyecto", max_length=200)