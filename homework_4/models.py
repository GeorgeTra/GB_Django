from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, description: {self.description}, price: {self.price}, ' \
               f'quantity: {self.quantity}, added: {self.add_date}.'

