from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class CustomMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 20
