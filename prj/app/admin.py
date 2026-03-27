from django.contrib import admin
from .models import KebabShop, Review

@admin.register(KebabShop)
class KebabShopAdmin(admin.ModelAdmin):
    # Co uvidíme v seznamu
    list_display = ('name', 'address', 'has_card_payment')
    # Podle čeho můžeme filtrovat
    list_filter = ('has_card_payment',)
    # Kde můžeme vyhledávat
    search_fields = ('name', 'address')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Přehledná tabulka recenzí
    list_display = ('author', 'kebab_shop', 'rating', 'created_at')
    # Filtrování podle hodnocení a podniku
    list_filter = ('rating', 'kebab_shop', 'created_at')
    # Vyhledávání v textu recenze a jménu autora
    search_fields = ('author', 'comment', 'kebab_shop__name')
    # Možnost rychle změnit hodnocení přímo v seznamu
    list_editable = ('rating',)