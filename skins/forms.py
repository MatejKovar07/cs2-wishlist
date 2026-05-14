from django import forms
from .models import Skin

class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['name', 'purchase_price', 'float_value', 'rarity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Např. AK-47 | Slate'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'float_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0000000001'}),
            'rarity': forms.Select(attrs={'class': 'form-select'}), # Toto vykreslí dropdown[cite: 4]
        }