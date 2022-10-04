from unittest.util import _MAX_LENGTH
from django.db import models
from api.models.fields import Fields
from api.models.service.ServiceCenter import ServiceCenter
class OrderHeader(models.Model):
    # Region Number
    regionKey = Fields.RegionField()
    # Sequence Number
    sequenceKey = models.CharField(max_length=6)
    # Addendum Number
    addendumKey = models.CharField(max_length=3)
    # Remote Svc Office
    serviceCenter = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE)
    # Gate Code
    #gateCode = models.CharField(max_length=15,default="",blank=True)
    # Open Site Y/N
    #openSite = models.BooleanField()
    # Requester Name
    requesterName = models.CharField(max_length=60)
    # Owner Name
    ownerName = models.CharField(max_length=60)
    # PO Number
    #poNumber = models.CharField(max_length=10)
    # Exclude Tax Yes/No
    #excludeTax = models.BooleanField()   
    # Est Labor Hrs
    laborHours = models.DecimalField(max_digits = 6,decimal_places=2)
    # Est Travel Hrs
    travelHours = models.DecimalField(max_digits = 6,decimal_places=2)
    # Estimated Trips
    trips = models.DecimalField(max_digits = 2, decimal_places=0)
    # Windbid Order Number
    #winBidOrder = models.CharField(max_length=8)
    # Techs Required
    techsRequired = models.BooleanField()
    # SpcTools Required
    #spcToolsRequired = models.BooleanField()    
    # Srvc Status
    status = models.CharField(max_length=4)
    # Srvc Sts Date
    statusDate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id) + '-' + str(self.sequenceKey) + '.' + str(self.addendumKey)
