from django.db import models
import api.models.fields.Regions as Regions, api.models.fields.ServiceCenter as ServiceCenter

class Technician(models.Model):
    # technician Indentifer
    techId = models.AutoField(primary_key=True, editable=False)
    # Primary Region
    primaryRegion = Regions.RegionField()
    # Primary Service Center
    primaryCenter = ServiceCenter.ServiceCenterField()
    # Tech Qualifier
    qualifier = models.CharField(max_length=1)
    # Tech Type E/V
    type = models.CharField(max_length=1)
    # Tech First Name
    firstName = models.CharField(max_length=128)
    # Tech Last Name
    lastName = models.CharField(max_length=128)
    # Tech Work Days (7 lsb for days of week)            (M T W TH F S S)
    workDays = models.SmallIntegerField(default=0x7C)   #(1 1 1  1 1 0 0) -> 0x7C
    # active
    active = models.BooleanField(default=True)