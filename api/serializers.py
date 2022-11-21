# LoginSerializer from https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/

from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import authenticate
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer, Profile
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
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'profile']




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


class OrderSequenceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order.OrderSequence
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    #startDateTime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    #endDateTime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    class Meta:
        model = Schedule.Schedule
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order.OrderItem
        fields = '__all__'


class OrderAddendumDetailSerializer(serializers.HyperlinkedModelSerializer):
    item_set = serializers.HyperlinkedRelatedField(
        view_name='item-detail',
        many=True,
        read_only=True,
    )

    schedule_set = serializers.HyperlinkedRelatedField(
        view_name='schedule-detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order.OrderAddendum
        fields = ['id', 'number', 'description', 'laborHours', 'travelHours',
                  'trips', 'status', 'statusDate', 'item_set', 'schedule_set']

# class OrderAddendumListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceCenter.ServiceCenter
#         fields = ['__str__','description','status', 'statusDate']


class OrderSequenceDetailSerializer(serializers.ModelSerializer):
    addendum_set = OrderAddendumDetailSerializer(many=True)

    class Meta:
        model = Order.OrderSequence
        fields = ['id', 'region', 'number', 'addendum_set']


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter.ServiceCenter
        fields = '__all__'


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician.Technician
        fields = '__all__'
