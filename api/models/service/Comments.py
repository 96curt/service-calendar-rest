from django.db import models
from django.conf import settings
from api import helper

from api.models.service.OrderHeader import OrderHeader


# Service Order Comments
class Comment(models.Model):
    #Service Order id
    serviceOrder = models.ForeignKey(OrderHeader, on_delete=models.CASCADE) 
    # Comment Type
    commentType = models.CharField(max_length=2)
    # Last Update By Id
    lastUpdateBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(helper.get_sentinel_user),
    )
    # Last Update Date
    updatedAt = models.DateTimeField(auto_now=True)
    # Comment/Note
    comment = models.CharField(max_length=2048)

    def __str__(self):
        return self.alias

    