from rest_framework import serializers
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='profile-detail',
        read_only=True,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'profile']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile.Profile
        fields = '__all__'


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
