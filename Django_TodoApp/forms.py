from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        labels = {
            'id': 'Order Id',
            'task': "task Information",
            'Done': "Task Status",
            'created_at': "Created At",
            'updated_at': "Updated At",
        }

        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'task': forms.TextInput(attrs={'placeholder': 'Buy carrots from supermarket.'}),
            'Done': forms.BooleanField(),
            'created_at': forms.DateTimeInput(attrs={'class': 'datepicker'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'datepicker'}),
        }