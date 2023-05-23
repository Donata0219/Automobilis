from django.db import models

# Create your models here.
class Automobilio_marke(models.Model):
    marke = models.CharField(max_length=20)
    modelis = models.CharField(max_length=100)

class Automobilis (models.Model):
    valstybinis_nr = models.CharField(max_length=20)
    automobilio_markes_id = models.ForeignKey(Automobilio_marke,
    on_delete = models.CASCADE)
    VIN_kodas = models.CharField(max_length=100)
    klientas = models.CharField(max_length=100)
