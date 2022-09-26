from django.db import models
from django.contrib.auth.models import User
from api.models.fields import Regions,ServiceCenter
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    region = Regions.RegionField()
    serviceCenter = ServiceCenter.ServiceCenterField()
    