# Generated by Django 4.2.7 on 2023-11-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('category_description', models.CharField(max_length=300, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Название')),
                ('product_description', models.CharField(max_length=300, verbose_name='Описание')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Фото')),
                ('category', models.CharField(max_length=150, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена за шт.')),
                ('data_created', models.DateField(verbose_name='Дата создания')),
                ('data_last_change', models.DateField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]