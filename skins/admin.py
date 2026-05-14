from django.contrib import admin
from .models import Skin

@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'purchase_price', 'current_price', 'is_owned')
    list_filter = ('is_owned', 'rarity')
    search_fields = ('name', 'user__username')