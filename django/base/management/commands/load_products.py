# your_app/management/commands/load_products.py

from django.core.management.base import BaseCommand
from base.models import Product
from base.products import products  # assuming your products list is in products.py

class Command(BaseCommand):
    help = 'Load product data into the database'

    def handle(self, *args, **options):
        for product_data in products:
            Product.objects.create(**product_data)
        self.stdout.write(self.style.SUCCESS('Successfully loaded product data'))
