from dataclasses import field
from django.db import models
from api.models.fields import Fields
from api.models.service.OrderHeader import OrderHeader
from api.models.service.Technician import Technician
from django.contrib.auth.models import User

#Service Order Schedule Model
class Schedule(models.Model):
    #Service Order id
    order = models.ForeignKey(OrderHeader)
    center = Fields.ServiceCenterField()
    scheduledBy = models.ForeignKey(User)
    scheduledDate = models.DateField()
    confirmed = models.BooleanField(default=False)
    confirmedBy = models.ForeignKey(User)
    description = models.CharField(max_length=1024, null=True)
    technician = models.ForeignKey(Technician)
    travelHours = models.DecimalField(max_digits=6, decimal_places=2)
    arrivalTime = models.DecimalField(max_digits=4)
    onSiteHours = models.DecimalField(max_digits=6, decimal_places=2)
    returnHours = models.DecimalField(max_digits=6, decimal_places=2)
    lunchTime = models.DecimalField(max_digits=4)