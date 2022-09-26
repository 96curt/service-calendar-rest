from django.db import models

# Service Order Comments
class Comments(models.Model):  
    # Sequence Number Two
    sequenceNumberTwo = models.IntegerField()
    # Key Date *Optional
    keyDate = models.DateField(null=True)
    # Comment Type
    commentType = models.CharField(max_length=1)
    # Last Update By Id
    lastUpdateById = models.IntegerField()
    # Last Update By Name
    lastUpdateByName = models.CharField(max_length=20)
    # Last Update Date
    lastUpdateDate = models.DateField()
    # Comment/Note
    comment = models.CharField(max_length=2048)