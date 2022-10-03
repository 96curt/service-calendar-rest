from django.db import models
from api.models.service.ServiceCenter import ServiceCenter
from api.models.service.OrderHeader import OrderHeader
from api.models.service.Technician import Technician
from api import helper
from django.conf import settings

# Service Order Schedule Model


class Schedule(models.Model):
    # Service Order id
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    # Service Center
    serviceCenter = models.ForeignKey(
        ServiceCenter,
        on_delete=models.CASCADE
    )
    # Who created the schedule
    scheduledBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(helper.get_sentinel_user),
        related_name='scheduledBy',
    )
    # When the schedule 
    scheduledDate = models.DateField()
    # Has the schedule been confirmed with customer.
    confirmed = models.BooleanField(default=False)
    # Who confirmed with the customer
    confirmedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(helper.get_sentinel_user),
        related_name='confirmedBy',
    )
    
    description = models.CharField(max_length=1024, null=True)
    technician = models.ForeignKey(
        Technician,
        on_delete=models.SET(helper.get_sentinel_tech),
    )
    travelHours = models.DecimalField(max_digits=6, decimal_places=2)
    arrivalTime = models.DecimalField(max_digits=4, decimal_places=0)
    onSiteHours = models.DecimalField(max_digits=6, decimal_places=2)
    returnHours = models.DecimalField(max_digits=6, decimal_places=2)
    lunchTime = models.DecimalField(max_digits=4, decimal_places=0)
