from django.contrib import admin
from .models import Contact

# admin.site.register(Company)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address_fact', 'vk', 'insta')
admin.site.register(Contact,ContactAdmin)