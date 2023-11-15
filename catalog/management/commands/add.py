from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.db import connection

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        list_products = [
            {
                "product_name": "Картофель",
                "product_description": "Картофель молодой",
                "product_image": "",
                #"category": 1,
                "price": 100,
                "data_created": "2023-11-14",
                "data_last_change": "2023-11-14"
            },
            {
                "product_name": "Редис",
                "product_description": "Редис прошлогодний",
                "product_image": "",

                "price": 120,
                "data_created": "2023-11-14",
                "data_last_change": "2023-11-14"
            },
            {
                "product_name": "Яблоки",
                "product_description": "Яблоки Семеренко",
                "product_image": "",

                "price": 150,
                "data_created": "2023-11-14",
                "data_last_change": "2023-11-14"
            },
            {
                "product_name": "Бананы",
                "product_description": "Бананы желтые",
                "product_image": "",

                "price": 60,
                "data_created": "2023-11-14",
                "data_last_change": "2023-11-14"
            }
        ]

        self.truncate_table_restart_id()

        for product in list_products:
            Product.objects.create(**product)

        print('Данные добавлены')

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE')
        print('Данные удалены')