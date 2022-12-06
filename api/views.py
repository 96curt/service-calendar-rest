from rest_framework import generics
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer, Region
from api import serializers
from api import filters
from rest_framework import permissions, views, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout
from drf_spectacular.utils import extend_schema

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @extend_schema(
        request=serializers.LoginSerializer
    )
    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProfileDetail(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    
    def get_object(self):
        return self.request.user


class CommentList(generics.ListAPIView):
    queryset = Comment.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CustomerList(generics.ListAPIView):
    queryset = Customer.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class OrderSequenceList(generics.ListAPIView):
    queryset = Order.OrderSequence.objects.all()
    serializer_class = serializers.OrderSequenceSerializer
    filterset_class = filters.OrderSequenceFilter

class OrderSequenceDetail(generics.RetrieveAPIView):
    queryset = Order.OrderSequence.objects.all()
    serializer_class = serializers.OrderSequenceSerializer


class OrderAddendumList(generics.ListAPIView):
    queryset = Order.OrderAddendum.objects.all()
    serializer_class = serializers.OrderAddendumSerializer
    filterset_class = filters.OrderAddendumFilter


class OrderAddendumDetail(generics.RetrieveAPIView):
    queryset = Order.OrderAddendum.objects.all()
    serializer_class = serializers.OrderAddendumSerializer


class ItemDetail(generics.RetrieveAPIView):
    queryset = Order.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class JobSiteList(generics.ListAPIView):
    queryset = JobSite.JobSite.objects.all()
    serializer_class = serializers.JobSiteSerializer


class JobSiteDetail(generics.RetrieveAPIView):
    queryset = JobSite.JobSite.objects.all()
    serializer_class = serializers.JobSiteSerializer

class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filterset_class = filters.ScheduleFilter


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    
class ScheduleExtra(generics.RetrieveAPIView):
    queryset = Schedule.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializerExtended


class ServiceCenterList(generics.ListAPIView):
    queryset = ServiceCenter.ServiceCenter.objects.all()
    serializer_class = serializers.ServiceCenterSerializer


class TechnicianList(generics.ListAPIView):
    queryset = Technician.Technician.objects.all()
    serializer_class = serializers.TechnicianSerializer
    filterset_class = filters.TechnicianFilter

class RegionList(generics.ListAPIView):
    queryset = Region.Region.objects.all()
    serializer_class = serializers.RegionSerializer