from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        list_categoryes = [
            {
              "category_name": "Fruits",
              "category_description": "Any fruits",
            },
            {
                "category_name": "Vegetables",
                "category_description": "Any Vegetables",
            },
        ]
        list_products = [
            {
                "product_name": "Potates",
                "product_description": "Potates 2023",
                "product_image": "catalog/potates.jpg",
                "category_id": 1,
                "price": 100,
                "data_created": "2023-01-01",
                "data_last_change": "2023-01-01"
            },
            {
                "product_name": "Carrot",
                "product_description": "Carrot 2023",
                "product_image": "catalog/carrot.jpg",
                "category_id": 1,
                "price": 60,
                "data_created": "2023-01-01",
                "data_last_change": "2023-01-01"
            },
            {
                "product_name": "Kiwi",
                "product_description": "Kiwi Egipet",
                "product_image": "catalog/kivi.jpg",
                "category_id": 2,
                "price": 150,
                "data_created": "2023-01-01",
                "data_last_change": "2023-01-01"
            },
            {
                "product_name": "Apple",
                "product_description": "Apple Semerenko",
                "product_image": "catalog/apple.jpg",
                "category_id": 2,
                "price": 110,
                "data_created": "2023-01-01",
                "data_last_change": "2023-01-01"
            },
            {
                "product_name": "Vinograd",
                "product_description": "Vinograd 2023",
                "product_image": "catalog/vinograd.jpg",
                "category_id": 2,
                "price": 200,
                "data_created": "2023-01-01",
                "data_last_change": "2023-01-01"
            }

        ]

        self.truncate_table_restart_id()

        for category in list_categoryes:
            Category.objects.create(**category)

        for product in list_products:
            Product.objects.create(**product)

        print('Данные добавлены')

    @classmethod
    def truncate_table_restart_id(cls):
        Product.objects.all().delete()
        print('Данные удалены')