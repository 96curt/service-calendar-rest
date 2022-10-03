from django.contrib import admin
from api.models.service import Comments,JobSite,OrderHeader,OrderItem,Schedule,ServiceCenter,Technician
from api.models import Customers, Profile

# Register your models here.

admin.site.register(Comments.Comment)
admin.site.register(JobSite.JobSite)
admin.site.register(OrderHeader.OrderHeader)
admin.site.register(OrderItem.OrderItem)
admin.site.register(Schedule.Schedule)
admin.site.register(ServiceCenter.ServiceCenter)
admin.site.register(Technician.Technician)
admin.site.register(Customers.Customer)
admin.site.register(Profile.Profile)
