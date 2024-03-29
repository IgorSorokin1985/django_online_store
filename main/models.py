from django.db import models
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True }

class ContactData(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.CharField(max_length=150, verbose_name='email')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Контакт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Контакты'  # Настройка для наименования набора объектов


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='text')
    blog_image = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='article_image')
    data_created = models.DateField(verbose_name='Data created', default='2023-01-01')
    data_published = models.DateField(verbose_name='Data published', default='2023-01-01')
    number_views = models.IntegerField(verbose_name='number of views', default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'article'  # Настройка для наименования одного объекта
        verbose_name_plural = 'articles'
        permissions = [
            (
                'work_with_articles',
                'Can add and correct articles'
            )
        ]
