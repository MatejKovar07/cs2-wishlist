from django.contrib import admin
from .models import Skin

@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    # Sloupce, které se zobrazí v přehledu v administraci
    list_display = ('nazev', 'uzivatel', 'cena', 'float_value', 'rarita', 'koupeno')
    
    # Filtry v pravém panelu administrace
    list_filter = ('koupeno', 'rarita')
    
    # Vyhledávací pole v administraci
    search_fields = ('nazev', 'uzivatel__username')