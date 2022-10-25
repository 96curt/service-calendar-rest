from rest_framework import generics
from api.models.service import Comment,JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer, Profile
from api import serializers


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class OrderSequenceList(generics.ListCreateAPIView):
    queryset = Order.OrderSequence.objects.all()
    serializer_class = serializers.OrderSequenceSerializer

class OrderAddendumList(generics.ListCreateAPIView):
    queryset = Order.OrderAddendum.objects.all()
    serializer_class = serializers.OrderAddendumSerializer

class OrderAddendumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.OrderAddendum.objects.all()
    serializer_class = serializers.OrderAddendumSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Order.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer

class JobSiteList(generics.ListCreateAPIView):
    queryset = JobSite.JobSite.objects.all()
    serializer_class = serializers.JobSiteSerializer

class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer


class ServiceCenterList(generics.ListCreateAPIView):
    queryset = ServiceCenter.ServiceCenter.objects.all()
    serializer_class = serializers.ServiceCenterSerializer


class TechnicianList(generics.ListCreateAPIView):
    queryset = Technician.Technician.objects.all()
    serializer_class = serializers.TechnicianSerializer
