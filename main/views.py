from catalog.models import Product
from main.models import ContactData, Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = ContactData
    template_name = 'main/contact.html'
    fields = ['name', 'email']
    extra_context = {
        'name': 'Contact'
    }
    success_url = reverse_lazy('contact_us')


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'text', 'blog_image', 'data_created', 'data_published']
    permission_required = 'main.work_with_articles'


    def get_success_url(self):
        return reverse('article_info', args=[self.object.slug])


class ArticleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Article
    template_name = 'main/article_info.html'
    permission_required = 'main.work_with_articles'

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


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        result = []
        for object in Article.objects.all():
            if object.is_published:
                result.append(object)

        context["object_list"] = sorted(result, key=lambda object: object.number_views, reverse=True)
        return context


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'main/article_form.html'
    fields = ['title', 'slug', 'text', 'blog_image', 'data_created', 'data_published', 'is_published']

    def get_success_url(self):
        return reverse('article_info', args=[self.object.slug])


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'main/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
