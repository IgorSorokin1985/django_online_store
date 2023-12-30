from django.shortcuts import render
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory

# Create your views here.

# Create your views here.
class ProductListView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'main/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_active=True).last()
            if active_version:
                object.active_version_number = active_version.number_version
                object.name_version = active_version.name_version
            else:
                object.active_version_number = None
        return context


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_info.html'
    success_url = reverse_lazy('product_list')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_success_url(self):
        return reverse('product_info', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)



class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/product_form.html'
    form_class = ProductForm


    def get_success_url(self):
        return reverse('product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
        else:
            formset = version_formset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
