from django.db import models
from api.models.Region import Region

class City(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.name