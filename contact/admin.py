from django.contrib import admin
from contact.models import *

class Contact_infoAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'keywords')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address_fact', 'vk', 'insta', 'inn', 'ogrn', 'kpp')

admin.site.register(Contact_info, Contact_infoAdmin)
admin.site.register(Contact, ContactAdmin)