from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ContactCreateView, ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [

    path('', ProductListView.as_view()),
    path('contact/', ContactCreateView.as_view(), name='contact_us'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_info/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('product_form/', ProductCreateView.as_view(), name='add_product'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article_info/<slug:slug>/', ArticleDetailView.as_view(), name='article_info'),
    path('article_form/', ArticleCreateView.as_view(), name='article_form'),
    path('article_update/<slug:slug>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='article_delete'),
]