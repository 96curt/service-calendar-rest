from django.db import models
from localflavor.us.models import USZipCodeField, USStateField

class AbstractLocation(models.Model):
    # Street Address
    street = models.CharField(max_length=1024)
    # Street Address line two
    street2 = models.CharField(max_length=1024, blank=True, default="")
    # City
    city = models.CharField(max_length=1024)
    # State
    state = USStateField()
    # zip code
    zipCode = USZipCodeField()
    # Country
    country = models.CharField(max_length=2, default="us")
    # County
    county = models.CharField(max_length=128)
    # Latitude
    latitude = models.FloatField(blank=True, null=True)
    # Longitude
    longitute = models.FloatField(blank=True, null=True)

    class meta:
        abstract = True