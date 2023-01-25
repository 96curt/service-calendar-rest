from django_filters import rest_framework as filters
from api.models.service import Schedule, Order, Technician, ServiceCenter, Manager
from api.models import Region, City, ZipCode


class ScheduleFilter(filters.FilterSet):
    startDateTime = filters.DateTimeFromToRangeFilter()
    endDateTime = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Schedule.Schedule
        fields = {
            'startDateTime': [],
            'endDateTime': [],
            'addendum__sequence__jobSite__region__id': ["exact"],
            'addendum__sequence__number': ["exact"],
            'addendum__number': ["exact"],
            'addendum__sequence__jobSite__zipCode': ["exact"],
            'addendum__sequence__jobSite__city': ["exact", "contains"],
            'serviceCenter__region__id': ["in"],
            'serviceCenter__region__managers__id': ["in"],
            'serviceCenter__id': ["in"],
            'serviceCenter__region__cities__id': ["in"],
            'serviceCenter__region__zipCodes__code': ["in"],
            'technicians__id': ["in"],
        }

class OrderAddendumFilter(filters.FilterSet):
    class Meta:
        model = Order.OrderAddendum
        fields = {
            'sequence__jobSite__region__id': ["in"],
            'sequence__manager__id': ["in"],
            'sequence__jobSite__region__centers__id': ["in"],
            'sequence__jobSite__region__cities__id': ["in"],
            'sequence__jobSite__region__zipCodes__code': ["in"],
            'sequence__jobSite__region__centers__technicians__id': ["in"],
            'sequence__number': ["exact"],
            'number': ["exact"],
            'status': ["exact"],
            'statusDate': ["exact"],
        }

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


class RegionFilter(filters.FilterSet):
    class Meta:
        model = Region.Region
        fields = {
            'name': ["contains"],
            'managers__id': ["in"]
        }


class ManagerFilter(filters.FilterSet):
    class Meta:
        model = Manager.Manager
        fields = {
            'firstName': ["contains"],
            'lastName': ["contains"],
            'region__id': ["in"]
        }


class CenterFilter(filters.FilterSet):
    class Meta:
        model = ServiceCenter.ServiceCenter
        fields = {
            'name': ["contains"],
            'region__id': ["in"],
            'region__managers__id': ["in"],
            'technicians__id': ["in"],
        }


class CityFilter(filters.FilterSet):
    class Meta:
        model = City.City
        fields = {
            'name': ["exact"],
            'region__id': ["in"],
            'region__managers__id': ["in"],
            'region__centers__id': ["in"],
        }


class ZipCodeFilter(filters.FilterSet):
    class Meta:
        model = ZipCode.ZipCode
        fields = {
            'code': ["exact"],
            'cities__name': ["contains"],
            'region__id': ["in"],
            'region__managers__id': ["in"],
            'region__centers__id': ["in"],
            'cities__id': ["in"],
        }


class TechnicianFilter(filters.FilterSet):
    class Meta:
        model = Technician.Technician
        fields = {
            'qualifier': ["exact"],
            'type': ["exact"],
            'workWeek': ["exact"],
            'firstName':  ["contains"],
            'lastName':  ["contains"],
            'centers__region__id': ["in"],
            'centers__region__managers__id': ["in"],
            'centers__id': ["in"],
            'centers__region__cities__id': ["in"],
            'centers__region__zipCodes__code': ["in"],
            'id': ["in"],
            
        }