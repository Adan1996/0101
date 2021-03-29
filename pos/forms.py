# from django import forms

# class Pos(forms.Form):
    

    # product_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Product name',
    #             'style': 'max-width: 25%;'
    #         }
    #     )
    # )

    # price = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Price',
    #             'style': 'max-width: 25%;',
    #             'type': 'number'
    #         }
    #     )
    # )

    # qty = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Quantity',
    #             'style': 'max-width: 25%;',
    #             'type': 'number'
    #         }
    #     )
    # )

from django import forms

from .models import PosModel

class Pos(forms.ModelForm):
    class Meta:
        model = PosModel
        fields = [
            'product_name',
            'price',
            'qty'
        ]