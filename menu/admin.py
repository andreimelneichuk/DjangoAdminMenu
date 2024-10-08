from django.contrib import admin
from .models import Menu, MenuItem
from django.core.exceptions import ValidationError

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

    def save_model(self, request, obj, form, change):
        if obj.parent == obj:
            raise ValidationError("Элемент не может быть родителем самого себя.")
        super().save_model(request, obj, form, change)