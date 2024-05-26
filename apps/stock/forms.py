from django import forms
from apps.stock.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['available', ]
        labels = {
            'name': 'Nome do Produto',
            'price': 'Preço do Produto',
            'description': 'Descrição do Produto',
            'inStock': 'Quantidade em Estoque',
            'available': 'Disponivel',
            'stockDate': 'Data de compra',
            'photo': 'Foto do produto, caso tenha',
            'user': 'Escolha a loja que realizou a compra'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'inStock': forms.NumberInput(attrs={'class': 'form-control'}),
            'stockDate': forms.DateTimeInput(format='%d/%m/%Y',
                                             attrs={'class': 'form-control',
                                                    'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),

        }
