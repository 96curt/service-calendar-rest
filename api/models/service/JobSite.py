from django.db import models

from api.models.abstract.AbstractLocation import AbstractLocation
from api.models.Customer import Customer
#from api.models.fields.Fields import RegionField
from api.models.Region import Region
class JobSite(AbstractLocation):
    #region = RegionField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.street + ' ' + self.street2 + ', ' + self.city + ', ' + self.state    