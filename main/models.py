from django.db import models

class ContactData(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.CharField(max_length=150, verbose_name='email')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Контакт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Контакты'  # Настройка для наименования набора объектов