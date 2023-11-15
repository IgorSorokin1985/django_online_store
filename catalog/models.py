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
    data_created = models.DateField(verbose_name='Дата создания', **NULLABLE)
    data_last_change = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.category}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов






