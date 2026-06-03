from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class SkinForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Např. AK-47 | Slate'})
    )
    purchase_price = forms.FloatField(
        validators=[MinValueValidator(0.0)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'})
    )
    float_value = forms.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0000000001', 'min': '0', 'max': '1'})
    )
    rarity = forms.ChoiceField(
        choices=[
            ('Consumer grade', 'Consumer grade'),
            ('Industrial grade', 'Industrial grade'),
            ('Mil-spec', 'Mil-spec'),
            ('Restricted', 'Restricted'),
            ('Classified', 'Classified'),
            ('Covert', 'Covert'),
            ('Special', '★ Special'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )