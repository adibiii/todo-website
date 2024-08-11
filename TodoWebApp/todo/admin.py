from django.contrib import admin
from django.contrib.admin import register

from todo.models import Todo


# Register your models here.
@register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', 'state']
    list_filter = ['state']
    search_fields = ('title',)

