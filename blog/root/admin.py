from django.contrib import admin

from root.models import Prof, Adv, Cat

admin.site.register(Prof)
admin.site.register(Cat)



class AdvertAdmin(admin.ModelAdmin):
  fielsds = ['author', 'header', 'name_cat', 'description', 'photo', 'date_pub']
  
  readonly_fields = ['author', 'date_pub']
  list_display = ('author', 'header', 'name_cat', 'date_pub')

# class CategoryAdmin(admin.ModelAdmin):
#   fields = ['id', 'name']
  
#   list_display = ('id', 'name')

admin.site.register(Adv, AdvertAdmin)
# admin.site.register(Cat, CategoryAdmin)