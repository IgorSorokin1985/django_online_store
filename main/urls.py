from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactCreateView, ArticleCreateView, ArticleListView, ArticleDetailView


urlpatterns = [

    path('', ProductListView.as_view()),
    path('contact.html', ContactCreateView.as_view(), name='contact_us'),
    path('product_list.html', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/product_info/', ProductDetailView.as_view(), name='product_info'),
    path('product_form.html', ProductCreateView.as_view(), name='add_product'),
    path('article_list.html', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/article_info/', ArticleDetailView.as_view(), name='article_info'),
    path('article_form.html', ArticleCreateView.as_view(), name='article_form'),
]