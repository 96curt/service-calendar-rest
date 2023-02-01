# LoginSerializer from https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/

from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import authenticate
from api.models.WorkWeek import WorkWeek
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician, Manager
from api.models import Customer, Profile, Region, City, ZipCode
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile.Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(many=False,read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment.Comment
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer.Customer
        fields = '__all__'


class JobSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSite.JobSite
        fields = '__all__'


class OrderSequenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order.OrderSequence
        fields = [
            'id',
            'number',
            'region',
            'jobSite',
            'name',
            'serviceCenter',
            'billingCust',
            'manager',
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    startDateTime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    endDateTime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    class Meta:
        model = Schedule.Schedule
        fields = [
            'id',
            'label',
            'startDateTime',
            'endDateTime',
            'confirmed',
            'description',
            'travelHours',
            'returnHours',
            'allDay',
            'recurrenceRule',
            'addendum',
            'serviceCenter',
            'scheduledBy',
            'confirmedBy',
            'technicians',
            'type',
            'addendumLaborHours',
            'addendumName',
            'billingCustName',
            'JobsiteAddress',
            'latitude',
            'longitude',
        ]
        


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order.OrderItem
        fields = '__all__'


class OrderAddendumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order.OrderAddendum
        fields = [
            'id',
            'number',
            'sequence',
            'name',
            'description',
            'trips',
            'travelHours',
            'laborHours',
            'status',
            'statusDate',
        ]


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter.ServiceCenter
        fields = [
            'id',
            'name',
            'region',
            'technicians',
        ]


class WorkWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkWeek
        fields = [
            'monday',
            'tuesday',
            'wedesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ]


class TechnicianSerializer(serializers.ModelSerializer):
    workWeek = WorkWeekSerializer(many=False)
    class Meta:
        model = Technician.Technician
        fields = [
            'id',
            'centers',
            'qualifier',
            'type',
            'firstName',
            'lastName',
            'fullName',
            'workWeek',
            'active',
            'schedules',
        ]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region.Region
        fields = [
            'id',
            'name',
            'managers',
        ]
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager.Manager
        fields = '__all__'

# class ScheduleSerializerExtended(serializers.ModelSerializer):
#     addendum = OrderAddendumSerializer(many=False)
#     serviceCenter = ServiceCenterSerializer(many=False)
#     scheduledBy = UserSerializer(many=False)
#     confirmedBy = UserSerializer(many=False)
#     technicians = TechnicianSerializer(many=True)

#     class Meta:
#         model = Schedule.Schedule
#         fields = [
#             'id',
#             'description',
#             'startDateTime',
#             'endDateTime',
#             'addendum',
#             'serviceCenter',
#             'scheduledBy',
#             'confirmed',
#             'confirmedBy',
#             'technicians',
#             'travelHours',
#             'allDay',
#             'recurrenceRule',
#         ]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City.City
        fields = '__all__'

class ZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCode.ZipCode
        fields = '__all__'