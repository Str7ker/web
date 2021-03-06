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

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'name', 'position', 'phone', 'mail')

class We_predAdmin(admin.ModelAdmin):
    list_display = ('name_pred', 'img', 'text')

class DescriptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc')

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyw')

class AllPartnerAdmin(admin.ModelAdmin):
    list_display = ('name_part', 'img', 'text', 'number', 'email')

class LogoAdmin(admin.ModelAdmin):
    list_display = ('small_logo', 'logo', 'background')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Romb, RombAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Partner, PartAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(We_pred, We_predAdmin)
admin.site.register(Description, DescriptionsAdmin)
admin.site.register(Keywords, KeywordAdmin)
admin.site.register(AllPartner, AllPartnerAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Email, EmailAdmin)