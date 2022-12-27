from django.db import models
from localflavor.us.models import USZipCodeField, USStateField
from api.models import City,Region
class ZipCode(models.Model):
    code = USZipCodeField(primary_key=True)
    city = models.ForeignKey(City.City, on_delete=models.CASCADE)
    region = models.ForeignKey(Region.Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.code