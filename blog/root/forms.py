from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Adv


class AdvForm(forms.ModelForm):
  class Meta:
    fields = ['header', 'name_cat', 'description', 'photo']
    model = Adv
    labels = {
      'header': 'Название объявления',
      'name_cat': 'Раздел',
      'description': 'Описание',
      'photo': 'Фото'
    }

    widgets = {
      'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
      'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'type':'file'})
    }