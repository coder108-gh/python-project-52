from django.forms import ModelForm
from .models import Status, Label, Task


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {
            'name': 'Имя',
        }
        error_messages = {
            'name': {
                'max_length': 'Название слишком длинное!',
                'required': 'Это поле обязательно для заполнения',
                'unique': 'Task status с таким Имя уже существует.'
            },
        }


class StatusFormDelete(ModelForm):
    class Meta:
        model = Status
        fields = []
        labels = {}


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Имя',
        }
        error_messages = {
            'name': {
                'max_length': 'Название слишком длинное!',
                'required': 'Это поле обязательно для заполнения',
                'unique': 'Label с таким Имя уже существует.'
            },
        }


class LabelFormDelete(ModelForm):
    class Meta:
        model = Label
        fields = []
        labels = {}


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status'] #  ???
