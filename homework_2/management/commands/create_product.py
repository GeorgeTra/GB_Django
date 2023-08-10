from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **options):
        product = Product(name='Wallet', description='Crocodile leather wallet. Made in China.',
                          price=15_000, quantity=2)
        product.save()
        self.stdout.write(f'{product}')


