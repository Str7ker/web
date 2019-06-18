from django.contrib import admin
from movizor.models import *
class MapAdmin(admin.ModelAdmin):
    list_display = ('map_token', 'title', 'desc', 'keywords')

class Map_contactAdmin(admin.ModelAdmin):
    list_display = ('ico', 'text', 'info')

admin.site.register(Map, MapAdmin)
admin.site.register(Map_contact, Map_contactAdmin)
