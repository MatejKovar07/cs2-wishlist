from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Skin(models.Model):
    RARITY_CHOICES = [
        ('Consumer', 'Consumer Grade'),
        ('Industrial', 'Industrial Grade'),
        ('Mil-Spec', 'Mil-Spec Grade'),
        ('Restricted', 'Restricted'),
        ('Classified', 'Classified'),
        ('Covert', 'Covert'),
        ('Special', '★ Knife / ★ Gloves'),
    ]

    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.0)]
    )
    float_value = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        default=0.0
    )
    rarita = models.CharField(max_length=50, choices=RARITY_CHOICES)
    koupeno = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nazev} ({self.rarita})"