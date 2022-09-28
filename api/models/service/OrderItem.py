from django.db import models
from api.models.service.OrderHeader import OrderHeader

class OrderItem(models.Model):
    order = models.ForeignKey(OrderHeader)
    originalOrder = models.CharField(max_length=8)
    originalItem = models.DecimalField(max_digits=3)
    originalDesc = models.CharField(max_length=30)
    serviceCode = models.DecimalField(max_length=2)
    warrantyCode = models.CharField(max_length=1)
    

