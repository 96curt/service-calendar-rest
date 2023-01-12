from django.db import models

from api.models.abstract.AbstractLocation import AbstractLocation
from api.models.Customer import Customer
from api.models.Region import Region
from api.models.City import City
from api.models.ZipCode import ZipCode

class JobSite(AbstractLocation):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    @property
    def address(self):
        return self.street + (self.street2 if self.street2 else '' ) + ', ' + self.city + ', ' + self.state

    def __str__(self):
        return self.address
    
    def save(self, *args, **kwargs):
        if not City.objects.filter(name=self.city) :
            City.objects.create(name=self.city,region=self.region)
        if not ZipCode.objects.filter(code=self.zipCode):
            city = City.objects.filter(name=self.city)[0]
            ZipCode.objects.create(code=self.zipCode,city=city)
        super(JobSite,self).save(args,kwargs)