from datetime import timedelta
from django.db import models
from api.models.service.Order import OrderAddendum
from api.models.service.ServiceCenter import ServiceCenter
from api.models.service.Technician import Technician
from api.models.WorkWeek import WorkWeek
from api import helper
from django.utils import timezone
from django.conf import settings

# Service Order Schedule Model


class Schedule(models.Model):
    # Service Order id
    addendum = models.ForeignKey(
        OrderAddendum,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='schedule_set',
        db_column='addendum_id',
    )
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
    
    # Has the schedule been confirmed with customer.
    confirmed = models.BooleanField(default=False)
    # Who confirmed with the customer
    confirmedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(helper.get_sentinel_user),
        related_name='confirmedBy',
        blank=True,
        null=True,
    )
    
    description = models.CharField(max_length=1024, null=True)
    # multiple technicians can be scheduled to an appointment
    technicians = models.ManyToManyField(
        Technician
    )

    date = models.DateField(
        default=timezone.now
    )
    startTime = models.TimeField(
        default=timezone.now
    )
    endTime = models.TimeField(
        default=timezone.now
    )
    travelHours = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.date.strftime('%m/%d/%Y') + ' ' +  self.startTime.strftime('%H:%M') 