from django.db import models
from api.models.fields import Fields
from api.models.service.JobSite import JobSite
from api.models.service.ServiceCenter import ServiceCenter
from api.models.service.Manager import Manager
from api.models.Customer import Customer
from api.models.Region import Region
# For each Job site a sequence is created.
class OrderSequence(models.Model):
    # Order Sequence Number
    number = models.PositiveSmallIntegerField(editable=False)
    # Region 
    ### region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # Jobsite Location
    jobSite = models.OneToOneField(JobSite, on_delete=models.CASCADE)
    # Assigned Service Center
    serviceCenter = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE)
    # Billing Customer
    billingCust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #Territory Manager
    manager = models.ForeignKey(
        Manager,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    @property
    def region(self):
        return self.jobSite.region.id

    @property
    def name(self):
        return str(self.region) + '-' + str(self.number)

    def __str__(self):
        return self.name()

    def save(self, *args, **kwargs):
        presentKeys = OrderSequence.objects.filter(models.Q(jobsite__region__id=self.jobSite.region.id)).order_by('-number').values_list('number', flat=True)
        if presentKeys:
            self.number = presentKeys[0] + 1    
        else:
            self.number = 1
        super(OrderSequence,self).save(args,kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['number', 'jobSite'], name='unique_sequence') 
        ]
    

# Each individual service request is an addendum and is related to a sequence.
class OrderAddendum(models.Model):
    # Order Addendum Number
    number = models.PositiveSmallIntegerField(editable=False)

    sequence = models.ForeignKey(
        OrderSequence,
        on_delete=models.CASCADE,
        related_name='addendum_set',
    )
    # Service request Description
    description = models.CharField(max_length = 128)
    # Est Labor Hours
    laborHours = models.DecimalField(max_digits = 6,decimal_places=2)
    # Est Travel Hrs
    travelHours = models.DecimalField(max_digits = 6,decimal_places=2)
    # Estimated Trips
    trips = models.DecimalField(max_digits = 2, decimal_places=0)
    # Srvc Status
    status = Fields.StatusCodeField(default='0')
    # Srvc Sts Date
    statusDate = models.DateField(auto_now=True)

    @property
    def name(self):
        return self.sequence.__str__() + '.' + str(self.number)

    def __str__(self):
        return self.name()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['number', 'sequence'], name='unique_addendum') 
        ]

    def save(self, *args, **kwargs):
        presentKeys = OrderAddendum.objects.filter(sequence=self.sequence).order_by('-number').values_list('number', flat=True)
        if presentKeys:
            self.number = presentKeys[0] + 1    
        else:
            self.number = 1
        super(OrderAddendum,self).save(args,kwargs)

# Any replacement parts that need to be ordered are an item and is related to an addendum
class OrderItem(models.Model):
    number = models.PositiveSmallIntegerField(editable=False)
    addendum = models.ForeignKey(
        OrderAddendum,
        on_delete=models.CASCADE,
        related_name='item_set' 
    )
    partOrder = models.CharField(max_length=8)
    partItem = models.DecimalField(max_digits=3, decimal_places=0)
    partDesc = models.CharField(max_length=30)
    serviceCode = Fields.ServiceCodeField()
    warrantyCode = Fields.WarrantyCodeField()

    def save(self, *args, **kwargs):
        presentKeys = OrderItem.objects.filter(addendum=self.addendum).order_by('-number').values_list('number', flat=True)
        if presentKeys:
            self.number = presentKeys[0] + 1    
        else:
            self.number = 1
        super(OrderItem,self).save(args,kwargs)
    
    def __str__(self): 
        return self.addendum.__str__() + '+' + str(self.number)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['number', 'addendum'], name='unique_item') 
        ]