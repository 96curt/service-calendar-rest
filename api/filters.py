from django.forms import ModelChoiceField
from django_filters import rest_framework as filters
from api.models.service import Schedule, Order, Technician


class ScheduleFilter(filters.FilterSet):
    startDateTime = filters.DateTimeFromToRangeFilter()
    endDateTime = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Schedule.Schedule
        fields = [
            'startDateTime',
            'endDateTime',
            'serviceCenter',
            'technicians',
            'addendum__sequence__region',
            'addendum__sequence__number',
            'addendum__number',
            'addendum__sequence__serviceCenter__manager',
            'addendum__sequence__jobSite__zipCode',
            'addendum__sequence__jobSite__city',
        ]

class OrderAddendumFilter(filters.FilterSet):
    class Meta:
        model = Order.OrderAddendum
        fields = [
            'sequence__region',
            'sequence__number',
            'number',
            'status',
            'statusDate',
        ]

class OrderSequenceFilter(filters.FilterSet):
    class Meta:
        model = Order.OrderSequence
        fields = [
            'region',
            'number',
        ]

class TechnicianFilter(filters.FilterSet):
    class Meta:
        model = Technician.Technician
        fields = [
            'primaryCenter',
            'primaryCenter__region',
            'primaryCenter__manager',
            'qualifier',
            'type',
            'workWeek',
        ]