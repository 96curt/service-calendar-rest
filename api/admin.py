from django.contrib import admin
from api.models.Customer import Customer
from api.models.Profile import Profile
from api.models.WorkWeek import WorkWeek
from api.models.service.Comment import Comment
from api.models.service.JobSite import JobSite
from api.models.service.Order import OrderAddendum, OrderSequence, OrderItem
from api.models.service.Schedule import Schedule
from api.models.service.ServiceCenter import ServiceCenter
from api.models.service.Technician import Technician
from api.models.Region import Region

# Register your models here.

admin.site.register(Comment)
admin.site.register(JobSite)
admin.site.register(OrderSequence)
admin.site.register(OrderAddendum)
admin.site.register(OrderItem)
admin.site.register(Schedule)
admin.site.register(ServiceCenter)
admin.site.register(WorkWeek)
admin.site.register(Technician)
admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Region)

