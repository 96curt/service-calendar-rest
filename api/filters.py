from django.forms import ModelChoiceField
from django_filters import rest_framework as filters
from api.models.service import Schedule, Order


class ScheduleFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Schedule.Schedule
        fields = [
            'date',
            'serviceCenter',
            'technicians',
            'startTime',
            'endTime',
            'addendum__sequence__region',
            'addendum__sequence__serviceCenter__manager',
            'addendum__sequence__jobSite__zipCode',
            'addendum__sequence__jobSite__city',
        ]

# class OrderAddendumFilter(filters.FilterSet):
#     class Meta:
#         model = Order.OrderAddendum
#         fields = ['sequence__number', 'number', 'status', 'statusDate']

# class OrderSequenceFilter(filters.FilterSet):
#     class Meta:
#         model = Order.OrderSequence
#         fields = ['region', 'number']