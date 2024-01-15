from django.shortcuts import render
from catalog.models import Product, Version, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from catalog.utils import get_categories


# Create your views here.


class ProductListView(LoginRequiredMixin, ListView):
    paginate_by = 6
    model = Product
    template_name = 'main/product_list.html'

    def get_queryset(self):
        product_list = super().get_queryset()
        if self.request.user.groups.filter(name='Модератор').exists():
            return product_list
        else:
            return product_list.filter(is_published=True)

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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_info.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = super().get_object()
        if self.object.owner == self.request.user or self.request.user.groups.filter(name='Модератор').exists() or self.request.user.is_superuser:
            context["edit"] = True
        else:
            context["edit"] = False
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'main/product_form.html'

    def get_form_class(self):
        if self.request.user.groups.filter(name='Модератор').exists():
            return ModeratorProductForm
        else:
            return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.request.user.groups.filter(name='Модератор').exists() or self.request.user.is_superuser:
            return self.object
        if self.object.owner != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def get_success_url(self):
        return reverse('product_info', args=[self.kwargs.get('pk')])

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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


def categories_list(request):
    context = {
        "objects_list": get_categories()
    }
    return render(request, 'main/categories_list.html', context=context)
