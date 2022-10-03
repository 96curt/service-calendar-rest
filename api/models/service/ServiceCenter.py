from django.db import models
from api.models.abstract.AbstractLocation import AbstractLocation

from api.models.fields import Fields

class ServiceCenter(AbstractLocation):
    name = models.CharField(max_length=128)
    region = Fields.RegionField()
    manager = Fields.TerritoryManagerField()



    