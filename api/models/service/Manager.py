from django.db import models
from api.models.Region import Region

class Manager(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    region = models.ManyToManyField(Region)
    def __str__(self):
        return self.firstName + ' ' + self.lastName