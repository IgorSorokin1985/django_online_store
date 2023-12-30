from django.urls import path
from main.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ContactCreateView


urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact_us'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article_info/<slug:slug>/', ArticleDetailView.as_view(), name='article_info'),
    path('article_form/', ArticleCreateView.as_view(), name='article_form'),
    path('article_update/<slug:slug>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='article_delete'),
]