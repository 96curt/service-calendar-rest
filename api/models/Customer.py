from django.db import models
from api.models.abstract.AbstractLocation import AbstractLocation

class Customer(AbstractLocation):
    # Billing Number
    #billingNumber = models.DecimalField(max_digits=3,decimal_places=0)
    # Contact First Name
    firstName = models.CharField(max_length=128)
    # Contact Last Name
    lastName = models.CharField(max_length=128)
    # Company Name
    companyName = models.CharField(max_length=256,blank=True,null=True)

    @property
    def name(self):
        return str(self.firstName) + ' ' + str(self.lastName)    

    def __str__(self):
        return self.name
