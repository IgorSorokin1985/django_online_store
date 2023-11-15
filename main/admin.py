from django.contrib import admin

from main.models import ContactData

@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')
