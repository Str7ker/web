from django.contrib import admin
from company.models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'small_text', 'big_text')

class Company_infoAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'keywords')

class CompanyNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'keywords')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Company_info, Company_infoAdmin)
admin.site.register(CompanyNews, CompanyNewsAdmin)