from django.contrib import admin

# Register your models here.
from .models import Mobile,Group

class MobileAdmin(admin.ModelAdmin):
    list_display = ('date', 
                    'name', 
                    'description', 
                    'price', 
                    'manager'
                    )
    list_editable = ('name', 'manager')
    search_fields = ('text',) 
    list_filter = ('name', 'manager', 'price') 
    empty_value_display = '-пусто-'

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 
                    'slug', 
                    'description', 
                    )
admin.site.register(Mobile, MobileAdmin) 
admin.site.register(Group, GroupAdmin)