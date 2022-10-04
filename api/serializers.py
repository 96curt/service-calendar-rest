from rest_framework import serializers
from api.models.service import Comment, JobSite, OrderHeader, OrderItem, Schedule, ServiceCenter, Technician
from api.models import Customer, Profile


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


class OrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader.OrderHeader
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem.OrderItem
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile.Profile
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule.Schedule
        fields = '__all__'


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter.ServiceCenter
        fields = '__all__'


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician.Technician
        fields = '__all__'
