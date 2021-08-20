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
			'header': forms.Textarea(attrs={
				'class': 'form-input',
				'placeholder': 'Заголовок',
				'rows':1
			}),
			'name_cat': forms.Select(attrs={
				'class': 'form-input',
			}),
			'description': forms.Textarea(attrs={
				'class': 'form-input',
				'placeholder': 'Описание',
				'cols': 2,
				'rows':5
			}),
			'photo': forms.ClearableFileInput(attrs={
				'class': 'form-control',
				'type':'file'
			})
		}