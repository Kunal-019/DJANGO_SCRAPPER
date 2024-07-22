from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    gdp = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    iso = models.CharField(max_length=100)
  

    class Meta:
        verbose_name_plural = "Country"



