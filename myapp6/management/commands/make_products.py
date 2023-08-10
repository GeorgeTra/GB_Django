from random import choice, randint, uniform
from homework_1.myapp5.models import Category, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate fake products.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для генерации.')

    def handle(self, *args, **options):
        category = Category.objects.all()
        count = options.get('count')
        products = []
        for i in range(1, count + 1):
            products.append(Product(
                name=f'Продукт номер {i}',
                category=choice(category),
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)

