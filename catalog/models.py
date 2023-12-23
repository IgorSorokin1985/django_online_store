from django.db import models

NULLABLE = {'blank': True, 'null': True }

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    category_description = models.CharField(max_length=300, verbose_name='Описание категории')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов

class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название')
    product_description = models.CharField(max_length=300, verbose_name='Описание')
    product_image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория ID', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за шт.')
    data_created = models.DateField(verbose_name='Дата создания', default='2023-01-01')
    data_last_change = models.DateField(verbose_name='Дата последнего изменения', default='2023-01-01')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.category}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.IntegerField(verbose_name="Номер версии")
    name_version = models.CharField(max_length=150, verbose_name="Название версии")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} {self.name_version}'

    class Meta:
        verbose_name = 'Версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Версии'  # Настройка для наименования набора объектов
        unique_together = (('number_version', 'product'),)
