# Generated by Django 4.2.7 on 2023-11-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='number_views',
            field=models.IntegerField(default=0, verbose_name='number of views'),
        ),
    ]
