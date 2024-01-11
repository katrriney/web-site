from .models import Zapis
from django.forms import ModelForm, TextInput, DateTimeInput, DateInput

class ZapisForm(ModelForm):
    class Meta:
        model = Zapis
        fields = ['FIO', 'date_bith', 'category', 'date', 'number']

        wid ={
            'FIO': TextInput(attrs={
                'class' : 'form-style',
                'placeholder' : 'ФИО',
            }),
            'date_bith': DateInput(attrs={
                'class': 'form-style',
                'placeholder': 'Дата рождения',
            }),
            'category': TextInput(attrs={
                'class': 'form-style',
                'placeholder': 'Категория врача',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-style',
                'placeholder': 'Дата и время записи',
            }),
            'number': TextInput(attrs={
                'class': 'form-style',
                'placeholder': 'Номер телефона',
            }),

        }
