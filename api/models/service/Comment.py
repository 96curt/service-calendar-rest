from urllib import request
from django.db import models
from django.conf import settings
from api import helper
from api.models.fields.Fields import CommentTypeField

from api.models.service.Order import OrderAddendum


# Service Order Comments
class Comment(models.Model):
    #Service Order id
    order = models.ForeignKey(OrderAddendum, on_delete=models.CASCADE) 
    # Comment Type
    commentType = CommentTypeField()
    # Last Update By Id
    lastUpdateBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(helper.get_sentinel_user),
    )
    # Last Update Date
    updatedAt = models.DateTimeField(auto_now=True, editable=False)

    # Comment/Note
    comment = models.CharField(max_length=2048)

    def __str__(self):
        return self.get_commentType_display() + ': ' + self.comment





    