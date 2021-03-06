from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'category')

admin.site.register(Page, PageAdmin)
admin.site.register(Category)

