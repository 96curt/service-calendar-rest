from django.db import models
from api.models.LocationBase import LocationBase

from api.models.fields import Fields

class ServiceCenter(LocationBase):
    name = models.CharField(max_length=128)
    region = Fields.RegionField()
    manager = Fields.TerritoryManagerField()



    