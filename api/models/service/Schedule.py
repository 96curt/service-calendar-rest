from datetime import timedelta, datetime
from django.utils import timezone
from django.db import models
from api.models.service.Order import OrderAddendum
from api.models.service.ServiceCenter import ServiceCenter
from api.models.service.Technician import Technician
from api.models.WorkWeek import WorkWeek
from api.models.fields import Fields
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
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='scheduledBy',
    )
    # Has the schedule been confirmed with customer.
    confirmed = models.BooleanField(default=False)
    # Who confirmed with the customer
    confirmedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='confirmedBy',
    )
    description = models.CharField(max_length=1024, null=True, blank=True)
    # multiple technicians can be scheduled to an appointment
    technicians = models.ManyToManyField(Technician, related_name='schedules')
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    travelHours = models.DecimalField(max_digits=6, decimal_places=2)
    returnHours = models.DecimalField(max_digits=6, decimal_places=2)
    allDay = models.BooleanField(default=False)
    recurrenceRule = models.CharField(blank=True,null=True,max_length=256)
    type = Fields.AppointmentTypeField(default='ORDR')

    @property
    def addendumLaborHours(self):
        return self.addendum.laborHours
    
    @property
    def addendumName(self):
        return self.addendum.name
    
    @property
    def billingCustName(self):
        return self.addendum.sequence.billingCust.name

    @property
    def JobsiteAddress(self):
        return self.addendum.sequence.jobSite.address

    @property
    def label(self):
        if(self.addendum):
            return ( 
                '(' + str(self.addendumLaborHours) + ') '
                + self.billingCustName + ', '
                + self.addendumName + ', '
                + self.JobsiteAddress
            )
        return self.description

    def __str__(self) -> str:
        return self.startDateTime.strftime('%m/%d/%Y-%H:%M') + ' ' + self.label

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.confirmedby = request.user
        super().save_model(request, obj, form, change)