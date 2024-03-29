from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, categories_list
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', ProductListView.as_view()),
    #path('contact/', ContactCreateView.as_view(), name='contact_us'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('categories_list/', categories_list, name='categories_list'),
    path('product_info/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_info'),
    path('product_form/', ProductCreateView.as_view(), name='add_product'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
