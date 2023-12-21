from django.contrib import admin

from main.models import ContactData, Article
from catalog.models import Version

@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number_version', 'name_version', 'is_active')

