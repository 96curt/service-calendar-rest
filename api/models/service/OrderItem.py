from django.db import models
from api.models.service.OrderHeader import OrderHeader
from api.models.fields import Fields

class OrderItem(models.Model):
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE )
    originalOrder = models.CharField(max_length=8)
    originalItem = models.DecimalField(max_digits=3,decimal_places=0)
    originalDesc = models.CharField(max_length=30)
    serviceCode = Fields.ServiceCodeField()
    warrantyCode = Fields.WarrantyCodeField()
    

