from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm
from .models import Product
import logging


logger = logging.getLogger(__name__)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Наименование']
            description = form.cleaned_data['Описание']
            price = form.cleaned_data['Цена']
            quantity = form.cleaned_data['Количество']
            image = form.cleaned_data['Фото']
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image)
            product.save()
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Загружен товар: {name}, описание: {description}, цена: {price}, количество: {quantity}.')
    else:
        form = ProductForm()
    return render(request, 'homework_4/product_form.html', {'form': form})






