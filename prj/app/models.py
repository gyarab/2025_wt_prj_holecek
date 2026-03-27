from django.db import models

class Kebabarna(models.Model):
    nazev = models.CharField(max_length=200)
    adresa = models.CharField(max_length=255)
    mesto = models.CharField(max_length=100)
    oteviraci_doba = models.CharField(max_length=100)
    email = models.EmailField()
    typ_masa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev

class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)
    heslo_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    
    oblibena_kebabarna = models.ForeignKey(
        Kebabarna, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='stali_zakaznici'
    )

    def __str__(self):
        return self.jmeno

class Recenze(models.Model):
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
    kebabarna = models.ForeignKey(Kebabarna, on_delete=models.CASCADE)
    
    hodnoceni_celkove = models.IntegerField()
    hodnoceni_maso = models.IntegerField()
    komentar = models.TextField()
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recenze od {self.uzivatel.jmeno} pro {self.kebabarna.nazev}"

class Fotografie(models.Model):
    recenze = models.ForeignKey(
        Recenze, 
        on_delete=models.CASCADE, 
        related_name='fotky'
    )
    url_odkaz = models.URLField(max_length=500)

    def __str__(self):
        return f"Foto k recenzi č. {self.recenze.id}"