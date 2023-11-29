from catalog.models import Product
from main.models import ContactData, Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

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


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'main/article_form.html'
    fields = ['title', 'slug', 'text', 'blog_image', 'data_created', 'data_published']


    #def get_context_data(self, **kwargs):
    #    context = super(ArticleCreateView, self).get_context_data(**kwargs)
    #    context['slug'] = slugify(kwargs['title'])
    #    return context


    def get_success_url(self):
        return reverse('article_info', args=[self.object.pk])

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/article_info.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.number_views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)

        if self.object.number_views == 100:
            send_mail(
                subject='Congratulations',
                message='Hello! Your article has 100 views',
                from_email=EMAIL_HOST_USER,
                recipient_list=['isorokin1985@gmail.com']
            )

        return self.render_to_response(context)


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        result = []
        for object in Article.objects.all():
            if object.is_published:
                result.append(object)

        context["object_list"] = sorted(result, key=lambda object: object.number_views, reverse=True)
        return context


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'main/article_form.html'
    fields = ['title', 'slug', 'text', 'blog_image', 'data_created', 'data_published', 'is_published']

    def get_success_url(self):
        return reverse('article_info', args=[self.object.pk])


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'main/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
