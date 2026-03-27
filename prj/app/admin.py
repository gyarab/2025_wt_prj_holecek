from django.contrib import admin
from .models import KebabShop, User, Recenze, Fotografie

# Registrace modelů do administrace
@admin.register(KebabShop)
class KebabShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'meat_type')
    search_fields = ('name', 'city')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')

@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
    list_display = ('uzivatel', 'kebabarna', 'hodnoceni_celkove', 'datum_vytvoreni')
    list_filter = ('hodnoceni_celkove', 'kebabarna')

@admin.register(Fotografie)
class FotografieAdmin(admin.ModelAdmin):
    list_display = ('id', 'recenze')