from django.db import models
from localflavor.us.models import USZipCodeField, USStateField
from api.models import City, Region
class ZipCode(models.Model):
    code = USZipCodeField(primary_key=True)
    cities = models.ManyToManyField(
        City.City,
        related_name="zipCodes",
    )
    region = models.ForeignKey(
        Region.Region,
        on_delete=models.CASCADE,
        related_name="zipCodes",
    )
    def __str__(self):
        return self.code