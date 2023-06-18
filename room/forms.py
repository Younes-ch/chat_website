from .models import Room

from django.forms.models import ModelForm
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                    'class': 'w-full mt-2 px-4 py-2 rounded-xl',
                    'placeholder': 'Enter room name...',
                    'autocomplete': 'off',
                    'autofocus': '',
                    'required': '',
                }),
        }

        labels = {
            'name': '',
        }