from django.db import models
from api.models.Profile import Profile
from api.models.fields.Regions import RegionField
from api.models.fields.ServiceCenter import ServiceCenterField
from api.models.service.OrderHeader import OrderHeader
from api.models.service.Technician import Technician

#Service Order Schedule Model
class Schedule(models.Model):
    #Service Order id
    orderId = models.ForeignKey(OrderHeader)
    region = RegionField()
    serviceCenter = ServiceCenterField()
    scheduledBy = models.ForeignKey(Profile)
    scheduledDate = models.DateField()
    technicianId = models.ForeignKey(Technician)
    travelHours = models.DecimalField(max_digits=6,decimal_places=2)
    arrivalTime = models.DecimalField(max_digits=4)
    onSiteHours = models.DecimalField(max_digits=6,decimal_places=2)
    returnHours = models.DecimalField(max_digits=6,decimal_places=2)
    lunchTime = models.DecimalField(max_digits=4)