from django.db import models

from api.models.abstract.AbstractLocation import AbstractLocation
from api.models.Customers import Customer
from api.models.fields.Fields import RegionField
class JobSite(AbstractLocation):
    region = RegionField()
    owner = models.ForeignKey(Customer,on_delete=models.CASCADE)
    