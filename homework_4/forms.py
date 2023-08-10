from django import forms


class ProductForm(forms.Form):
    Наименование = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Описание = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Введите описание товара'}))
    Цена = forms.DecimalField(max_digits=8, decimal_places=2)
    Количество = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Фото = forms.ImageField()


