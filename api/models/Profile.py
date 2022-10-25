from django.db import models
from django.contrib.auth.models import User
from api.models.fields.Fields import RegionField
from api.models.service.ServiceCenter import ServiceCenter
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    region = RegionField()
    serviceCenter = models.ForeignKey(ServiceCenter, on_delete=models.SET_NULL,null=True)
    
    def __str__(self) -> str:
        return self.user.__str__()