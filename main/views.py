from django.shortcuts import render
from catalog.models import Product
from main.models import ContactData
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class ProductListView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'main/product_list.html'
    extra_context = {
        'objects_list': Product.objects.all()
    }

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_info.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    fields = ['product_name', 'product_description', 'product_image', 'category', 'price']
    success_url = reverse_lazy('product_list')


class ContactCreateView(CreateView):
    model = ContactData
    template_name = 'main/contact.html'
    fields = ['name', 'email']
    extra_context = {
        'name': ContactData.objects.get(pk=1)
    }
    success_url = reverse_lazy('contact_us')

