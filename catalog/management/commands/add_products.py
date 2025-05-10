from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Хозяйство')

        products = [
            {'name': 'Салфетки', 'description': 'Для столов', 'price': '99.99', 'category': category},
            {'name': 'Кубики', 'description': 'Для стирки', 'price': '849.99', 'category': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))
