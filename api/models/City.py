from django.db import models
from api.models.Region import Region
from localflavor.us.models import USZipCodeField, USStateField

class City(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="cities",
    )
    # State
    state = USStateField()
    # Country
    country = models.CharField(max_length=2, default="us")
    # County
    county = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name + ', ' + self.state

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'state', 'country'], name='unique_city') 
        ]