from rest_framework import generics
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer, Profile
from django.contrib.auth.models import User
from rest_framework import permissions
from api import serializers
from api import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

class profileDetail(generics.RetrieveAPIView):
    queryset = Profile.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'
    permission_class = permissions.IsAuthenticated
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CustomerList(generics.ListAPIView):
    queryset = Customer.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class OrderSequenceList(generics.ListAPIView):
    queryset = Order.OrderSequence.objects.all()
    serializer_class = serializers.OrderSequenceListSerializer

class OrderSequenceDetail(generics.RetrieveAPIView):
    queryset = Order.OrderSequence.objects.all()
    serializer_class = serializers.OrderSequenceDetailSerializer

# class OrderAddendumList(generics.ListAPIView):
#     queryset = Order.OrderAddendum.objects.all()
#     serializer_class = serializers.Order
#     filterset_class = filters.OrderAddendumFilter

class OrderAddendumDetail(generics.RetrieveAPIView):
    queryset = Order.OrderAddendum.objects.all()
    serializer_class = serializers.OrderAddendumDetailSerializer


class ItemDetail(generics.RetrieveAPIView):
    queryset = Order.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class JobSiteList(generics.ListAPIView):
    queryset = JobSite.JobSite.objects.all()
    serializer_class = serializers.JobSiteSerializer


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filterset_class = filters.ScheduleFilter

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer

class ServiceCenterList(generics.ListAPIView):
    queryset = ServiceCenter.ServiceCenter.objects.all()
    serializer_class = serializers.ServiceCenterSerializer
    


class TechnicianList(generics.ListAPIView):
    queryset = Technician.Technician.objects.all()
    serializer_class = serializers.TechnicianSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'admin': reverse('admin:index',request=request, format=format),
        'swagger-ui': reverse('swagger-ui',request=request, format=format),
    })