# Generated by Django 4.2.7 on 2023-11-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateField(default='2023-01-01', verbose_name='Дата создания'),
        ),
    ]
