from django.db import models

from api.models.LocationBase import LocationBase
from api.models.Customers import Customer
from api.models.fields.Regions import RegionField
class JobSite(LocationBase):
    region = RegionField()
    customer = models.ForeignKey(Customer)
    