from django.contrib import admin
from team.models import *

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'name', 'position', 'phone', 'mail')

class TextTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Teams, TeamAdmin)
admin.site.register(TextTeam, TextTeamAdmin)
