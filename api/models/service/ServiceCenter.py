from django.db import models
from api.models.abstract.AbstractLocation import AbstractLocation
from api.models.Region import Region

class ServiceCenter(AbstractLocation):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="centers")

    # Many to Many Relations: technicians

    def __str__(self):
        return self.name
