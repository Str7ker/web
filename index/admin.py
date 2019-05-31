from django.contrib import admin
from index.models import *


# admin.site.register(Company)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address_fact', 'vk', 'insta')

class RombAdmin(admin.ModelAdmin):
    list_display = ('name_romb', 'ico', 'text', 'numbers')

class CarAdmin(admin.ModelAdmin):
    list_display = ('name_cars', 'img', 'name', 'text')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name_work', 'img', 'name', 'text')

class PartAdmin(admin.ModelAdmin):
    list_display = ('name_part', 'img')

class We_predAdmin(admin.ModelAdmin):
    list_display = ('name_pred', 'img', 'text')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Romb, RombAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Partner, PartAdmin)
admin.site.register(We_pred, We_predAdmin)
