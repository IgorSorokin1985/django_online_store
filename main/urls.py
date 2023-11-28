from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactCreateView


urlpatterns = [

    path('', ProductListView.as_view()),
    #path('contact.html', contact_us, name='contact_us'),
    path('contact.html', ContactCreateView.as_view(), name='contact_us'),
    path('product_list.html', ProductListView.as_view(), name='product_list'),

    path('<int:pk>/product_info/', ProductDetailView.as_view(), name='product_info'),
    #path('add_product', add_product, name='add_product'),
    path('product_form.html', ProductCreateView.as_view(), name='add_product')
]