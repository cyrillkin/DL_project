from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea

from root.models import Prof, Adv, Cat


admin.site.unregister(User)


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
	fieldsets =[
		('About', {'fields': ['author']}),
		('About advert', {'fields': ['name_cat', 'header', 'photo', 'description']}),
		('Date information', {'fields': ['date_pub']})
	]
	readonly_fields = ['date_pub']
	list_display = ('author', 'header', 'description', 'date_pub')
	search_fields = ['header', 'description']
	list_filter = ['header', 'date_pub']
	actions = ['description_empty']

	@staticmethod
	def description_empty(modeladmin, request, queryset):
		""" Сделать все описания пустыми """    

		for descr in queryset:
			descr.description = ''
			descr.save()


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
	fieldsets =[
	('Name category', {'fields': ['name']}),
	]
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 20})}
	}  
	list_display = ('id', 'name')


class ProfInline(admin.StackedInline):
	model = Prof
	fieldsets =[
		('About', {'fields': ['user', 'birth_date', 'avatar']}),
		('Others information', {'fields': ['city', 'description']}),
	]

@admin.register(User)
class UserAdmin(UserAdmin):
	inlines = [ProfInline]