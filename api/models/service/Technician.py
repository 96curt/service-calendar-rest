from datetime import datetime, time
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

from api.models.service.ServiceCenter import ServiceCenter
from api.models.WorkWeek import WorkWeek, get_sentinel_workWeek

class Technician(models.Model):
    # Primary Service Center
    primaryCenter = models.ForeignKey(ServiceCenter, on_delete=models.SET_NULL, null=True)
    # Tech Qualifier
    qualifier = models.CharField(max_length=1,default="0")
    # Tech Type E/V
    type = models.CharField(max_length=1,default="0")
    # Tech First Name
    firstName = models.CharField(max_length=128)
    # Tech Last Name
    lastName = models.CharField(max_length=128, default="")
    # Tech Work Days 
    workWeek = models.ForeignKey(WorkWeek,on_delete=models.SET_NULL,null=True)
    # active
    active = models.BooleanField(default=True)
    #lunch time
    #lunchTime = models.TimeField(
    #    default = time(hour=12)
    #)

    def fullName(self) -> str:
        return self.firstName + ' ' + self.lastName

    def __str__(self) -> str:
        return self.fullName()

        