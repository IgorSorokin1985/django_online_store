from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        list_products = [
            {
                "product_name": "Картофель",
                "product_description": "Картофель молодой",
                "product_image": "",

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

        for product in list_products:
            Product.objects.create(**product)