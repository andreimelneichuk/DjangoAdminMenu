from django.contrib import admin
from .models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'url', 'url_name', 'order')
    list_filter = ('menu', 'parent')
    ordering = ('menu', 'parent', 'order')
    autocomplete_fields = ('parent',)
    search_fields = ('title', 'url', 'url_name') 