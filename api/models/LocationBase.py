from django.db import models
from localflavor.us.models import USZipCodeField, USStateField
class LocationBase(models.Model):
    # Street Address
    street = models.CharField(max_length=1024)
    # Street Address line two
    street2 = models.CharField(max_length=1024)
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
    latitude = models.FloatField(null=True)
    # Longitude
    longitute = models.FloatField(null=True)

    class meta:
        abstract = True