from django.db import models

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
    slug = models.CharField(max_length=150, verbose_name='slug')
    text = models.TextField(verbose_name='text')
    blog_image = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='article_image')
    data_created = models.DateField(verbose_name='Data created', default='2023-01-01')
    data_published = models.DateField(verbose_name='Data published', default='2023-01-01')
    number_views = models.IntegerField(verbose_name='number of views', default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'article'  # Настройка для наименования одного объекта
        verbose_name_plural = 'articles'
