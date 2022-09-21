from django.db import models
import LocationBase
import uuid

class Customer(LocationBase):
    # Customer Number
    customerId = models.AutoField(primary_key=True, editable=False)
    
    # Billing Number
    billingNumber = models.IntegerFields()
    # Contact First Name
    firstName = models.CharField(max_length=128)
    # Contact Last Name
    lastName = models.CharField(max_length=128)
    # Company Name
    companyName = models.CharField(max_length=256)
    

