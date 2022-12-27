from django_filters import rest_framework as filters
from api.models.service import Schedule, Order, Technician, ServiceCenter, Manager
from api.models import Region, City, ZipCode


class ScheduleFilter(filters.FilterSet):
    startDateTime = filters.DateTimeFromToRangeFilter()
    endDateTime = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Schedule.Schedule
        fields = {
            'startDateTime': ["range"],
            'endDateTime': ["range"],
            'serviceCenter__id': ["exact"],
            'technicians__id':["in"],
            'addendum__sequence__jobSite__region__id': ["exact"],
            'addendum__sequence__number': ["exact"],
            'addendum__number': ["exact"],
            'addendum__sequence__jobSite__zipCode': ["exact"],
            'addendum__sequence__jobSite__city': ["exact", "contains"],
        }

class OrderAddendumFilter(filters.FilterSet):
    class Meta:
        model = Order.OrderAddendum
        fields = [
            'sequence__jobSite__region__id',
            'sequence__number',
            'number',
            'status',
            'statusDate',
        ]

class OrderSequenceFilter(filters.FilterSet):
    class Meta:
        model = Order.OrderSequence
        fields = [
            'jobSite__region__id',
            'number',
            'jobSite',
            'serviceCenter',
            'billingCust',
        ]


class TechnicianFilter(filters.FilterSet):
    class Meta:
        model = Technician.Technician
        fields = {
            'centers__id': ["in"],
            'centers__region__id': ["in", "exact"],
            'qualifier': ["exact"],
            'type': ["exact"],
            'workWeek': ["exact"],
            'firstName':  ["contains"],
            'lastName':  ["contains"],
        }

class CenterFilter(filters.FilterSet):
    class Meta:
        model = ServiceCenter.ServiceCenter
        fields = {
            'region__id': ["in"],
            'name': ["contains"]
        }

class RegionFilter(filters.FilterSet):
    class Meta:
        model = Region.Region
        fields = {
            'name': ["contains"]
        }

class ManagerFilter(filters.FilterSet):
    class Meta:
        model = Manager.Manager
        fields = {
            'firstName': ["contains"],
            'lastName': ["contains"],
            'region__id': ["in"]
        }

class CityFilter(filters.FilterSet):
    class Meta:
        model = City.City
        fields = {
            'name': ["exact"],
            'region__id': ["in"]
        }
class ZipCodeFilter(filters.FilterSet):
    class Meta:
        model = ZipCode.ZipCode
        fields = {
            'code': ["exact"],
            'city__name': ["contains"],
            'city__id': ["in"],
            'region__id': ["in"]
        }