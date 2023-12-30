from django.core.management.base import BaseCommand
from myapp.models import Category, Product, Order, Customer, Review
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))

        # Create Categories
        categories = ['Electronics', 'Clothing', 'Books', 'Home Goods']
        for category_name in categories:
            Category.objects.create(name=category_name)

        # Create Products
        for i in range(20):
            product = Product.objects.create(
                name=f'Product {i+1}',
                description=f'Description for Product {i+1}',
                category=Category.objects.order_by('?').first()
            )

        # Create Customers
        for i in range(10):
            Customer.objects.create(
                name=f'Customer {i+1}',
                email=f'customer{i+1}@example.com'
            )

        # Create Orders
        for i in range(10):
            order = Order.objects.create(order_date='2023-01-01')
            products = Product.objects.order_by('?')[:3]
            order.products.set(products)

        # Create Reviews
        for product in Product.objects.all():
            Review.objects.create(
                text=f'Review for {product.name}',
                rating=5,
                product=product
            )

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
