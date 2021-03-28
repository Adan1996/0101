from django import forms

class TypeForm(forms.Form):
    type_alfabet = forms.CharField(
                        max_length=100,
                        widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'style': 'max-width: 50%;',
                                'placeholder': 'Alfabet'
                            }
                        )
                    )
    
    sentence = forms.CharField(
                        max_length=100,
                        widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'style': 'max-width: 50%;',
                                'placeholder': 'Sentence'
                            }
                        )
                    )