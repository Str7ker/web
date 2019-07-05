from django.contrib import admin
from adminpanel.models import *


# admin.site.register(Company)
class Admin_mainAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'url', 'count', 'color', 'ico')

admin.site.register(Admin_main, Admin_mainAdmin)