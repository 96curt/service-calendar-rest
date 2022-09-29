from django.db import models
from django.contrib.auth.models import User

from api.models.service.OrderHeader import OrderHeader

# Service Order Comments
class Comments(models.Model):
    #Service Order id
    serviceOrder = models.ForeignKey(OrderHeader) 
    # Comment Type
    commentType = models.CharField(max_length=2)
    # Last Update By Id
    lastUpdateBy = models.ForeignKey(User)
    # Last Update Date
    lastUpdateDate = models.DateField()
    # Comment/Note
    comment = models.CharField(max_length=2048)