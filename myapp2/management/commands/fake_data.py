from django.core.management.base import BaseCommand
from ...models import Author, Post


class Command(BaseCommand):
    help = "Create fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(title=f'Title{j}', content=f'Text from {author.name} #{j} is bla-bla-bla'
                                                       f'very long text', author=author)
                post.save()

