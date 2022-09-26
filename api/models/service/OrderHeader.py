from django.db import models
from api.models.fields.Regions import RegionField
from api.models.fields.ServiceCenter import ServiceCenterField

class OrderHeader(models.Model):
    # Region Number
    regionKey = RegionField()
    # Sequence Number
    sequenceKey = models.IntegerField()
    # Addendum Number
    addendumKey = models.IntegerField()
    # Current Region
    curRegion = RegionField()
    # Current Terr Mgr
    curTerritoryManager = models.CharField(max_length=3)
    # Remote Svc Office
    remoteServiceCenter = ServiceCenterField()
    # Gate Code
    gateCode = models.CharField(max_length=15)
    # Open Site Y/N
    openSite = models.BooleanField()
    # Requester Name
    requesterName = models.CharField(max_length=60)
    # Owner Name
    ownerName = models.CharField(max_length=60)
    # PO Number
    poNumber = models.CharField(max_length=10)
    # Exclude Tax Yes/No
    excludeTax = models.BooleanField()   
    # Est Labor Hrs
    laborHours = models.IntegerField()
    # Est Travel Hrs
    travelHours = models.IntegerField()
    # Estimated Trips
    trips = models.IntegerField()
    # Windbid Order Number
    winBidOrder = models.CharField(max_length=8)
    # Techs Required
    techsRequired = models.BooleanField()
    # SpcTools Required
    spcToolsRequired = models.BooleanField()    
    # Srvc Status
    status = models.CharField(max_length=4)
    # Srvc Sts Date
    statusDate = models.DateField()
