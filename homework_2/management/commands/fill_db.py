from django.core.management.base import BaseCommand
from random import choices
from ...models import Client, Product, Order

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur \
consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeat \
quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa \
ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, \
laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium \
assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum \
expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque \
nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit \
vero vitae voluptates."


class Command(BaseCommand):
    help = 'Generate fake clients and products.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client id')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Client_{i}', email=f'mail{i}mail.ru', phone=f'Phone_number: {i}-xxx-xxx-xxx',
                            address=f'Address: {i}, Street {i}, City {i}')
            client.save()
            for j in range(1, count + 1):
                product = Product(name=f'Product_name: {j}',
                                  description=" ".join(choices(text, k=10)),
                                  price=i * 100,
                                  quantity=i
                                  )
                product.save()
