from django.db import models

# Service Order Abstract Base Model
class ServiceBase(models.Model):
    # Region Number
    regionKey = models.IntegerField()
    # Sequence Number
    sequenceKey = models.IntegerField()
    # Addendum Number
    addendumKey = models.IntegerField()

    class meta:
        abstract = True