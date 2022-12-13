from django.db import models
from api.models.abstract.AbstractLocation import AbstractLocation
from api.models.Region import Region
from api.models.fields import Fields

class ServiceCenter(AbstractLocation):
    name = models.CharField(max_length=128)
    #region = Fields.RegionField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    manager = Fields.TerritoryManagerField()

    def __str__(self):
        return self.name

    