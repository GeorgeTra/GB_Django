from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ('name', 'price', 'quantity')
    ordering = ['price', '-quantity']
    list_filter = ['add_date', 'price']
    search_fields = ['description']
    search_help_text = ['Найти по слову в описании товара']
    actions = [reset_quantity]
    """Отдельный продукт."""
    fields = ['name', 'description', 'price', 'quantity', 'add_date']
    readonly_fields = ['add_date', 'description']


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['order_date']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'description': 'ФИО клиента',
                'fields': ['client']
            },
        ),
        (
            'Товары',
            {
                'classes': ['collapse'],
                'description': 'Наименования товаров и общая цена заказа',
                'fields': ['products', 'total_price']
            },
        ),
        (
            'Дата заказа',
            {
                'classes': 'wide',
                'fields': ['order_date']
            },
        )
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)





