from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = 'Create client.'

    def handle(self, *args, **options):
        client = Client(name='George Trakhtenberg', email='george_t@mail.com', phone='8-991-567-45-90',
                        address='3, Lesnaya str., Moscow, 323009')
        client.save()
        self.stdout.write(f'{client}')



