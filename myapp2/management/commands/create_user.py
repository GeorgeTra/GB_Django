from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **kwargs):
        user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user.save()
        self.stdout.write(f'{user}')

