from datetime import datetime
from django.db import models
import arrow

# Create your models here.

CategoryPlans = [
    ('VC', 'Viajes Cortos'),
    ('AMV', 'Anual Multiviaje'),
    ('LE', 'Larga Estadia'),
]

Destination = [
    ('LC', 'Local'),
    ('EUR', 'Europa'),
    ('WW', 'Resto del mundo'),
]

numPax = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
]

typeDocument = [
    ('CC', 'Cedula de Ciudadania'),
    ('TI', 'Tarjeta de Identidad'),
    ('CE', 'Cedula de Extranjeria'),
]


class CountryOrigin(models.Model):
    prefix = models.CharField(max_length=5)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CountryDestination(models.Model):
    prefix = models.CharField(max_length=5)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TypeDocument(models.Model):
    prefix = models.CharField(max_length=5)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cotizador(models.Model):
    categoryplans = models.ForeignKey(CategoryPlan, on_delete=models.PROTECT)
    origin = models.ForeignKey(CountryOrigin, on_delete=models.PROTECT)
    destination = models.ForeignKey(
        CountryDestination, on_delete=models.PROTECT)
    dates = models.CharField(max_length=255)
    numPax = models.CharField(max_length=255, choices=numPax)
    typeDocument = models.ForeignKey(TypeDocument, on_delete=models.PROTECT)
    numdocument = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.origin.name

    def dates_as_list(self):
        splits = self.dates.split("-")
        one = ""
        two = ""

        print(one, two)

        one = splits[0]
        two = splits[1]

        # arrow.format('MM/DD/YYYY')
        a = arrow.get(one, 'MM/DD/YYYY')
        b = arrow.get(two, 'MM/DD/YYYY')

        delta = (b-a)
        print(delta.days)

        return self.dates.split("-")
