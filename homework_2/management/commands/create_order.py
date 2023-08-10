from django.core.management.base import BaseCommand
from ... models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order.'

    def handle(self, *args, **options):
        order = Order(client=Client, products=Product, total_price=15_000_000)
        order.save()
        self.stdout.write(f'{order}')