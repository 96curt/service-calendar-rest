from django.db import models

from api.models.LocationBase import LocationBase
from api.models.Customers import Customer
class JobSite(LocationBase):

    jobSiteId = models.AutoField(primary_key=True, editable=False)

    customer = models.ForeignKey(Customer)