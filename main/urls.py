from django.urls import path
from main.views import index, contact_us

urlpatterns = [
    path('', index),
    path('contact.html', contact_us),
    path('index.html', index),
]