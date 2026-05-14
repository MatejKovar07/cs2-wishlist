from django.db import models
from django.contrib.auth.models import User

class Skin(models.Model):
    # Definice rarit pro dropdown menu[cite: 3]
    RARITY_CHOICES = [
        ('Consumer Grade', 'Consumer Grade (Bílá)'),
        ('Industrial Grade', 'Industrial Grade (Světle modrá)'),
        ('Mil-Spec', 'Mil-Spec (Tmavě modrá)'),
        ('Restricted', 'Restricted (Fialová)'),
        ('Classified', 'Classified (Růžová)'),
        ('Covert', 'Covert (Červená)'),
        ('Contraband', 'Contraband (Oranžová)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rarity = models.CharField(max_length=50, choices=RARITY_CHOICES) # Propojení s choices[cite: 3]
    float_value = models.FloatField(default=0.0)
    is_owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name