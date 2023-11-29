from django.contrib import admin

from main.models import ContactData, Article

@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text')
