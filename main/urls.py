from django.urls import path
from main.views import index, contact_us, product_info, add_product

urlpatterns = [
    path('', index),
    path('contact.html', contact_us, name='contact_us'),
    path('index.html', index, name='index'),
    path('<int:pk>/product_info/', product_info, name='product_info'),
    path('add_product', add_product, name='add_product')
]