from django.db import models

class KebabShop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)
    email = models.EmailField()
    meat_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    avatar_url = models.URLField(max_length=500, blank=True, null=True)

    favorite_kebab_shop = models.ForeignKey(
        KebabShop, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='stali_zakaznici'
    )

    def __str__(self):
        return self.username

class Recenze(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    kebabarna = models.ForeignKey(KebabShop, on_delete=models.CASCADE)
    
    hodnoceni_celkove = models.IntegerField()
    hodnoceni_maso = models.IntegerField()
    komentar = models.TextField()
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recenze od {self.uzivatel.username} pro {self.kebabarna.name}"

class Fotografie(models.Model):
    recenze = models.ForeignKey(
        Recenze, 
        on_delete=models.CASCADE, 
        related_name='fotky'
    )
    url_odkaz = models.URLField(max_length=500)

    def __str__(self):
        return f"Foto k recenzi č. {self.recenze.id}"
    