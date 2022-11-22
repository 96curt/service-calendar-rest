from rest_framework import generics
from api.models.service import Comment, JobSite, Order, Schedule, ServiceCenter, Technician
from api.models import Customer
from api import serializers
from api import filters
from rest_framework import permissions, views, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import login, logout
from drf_spectacular.utils import extend_schema


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

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
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProfileDetail(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    
    def get_object(self):
        return self.request.user


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



def api_root(request, format=None):
    return Response({
        'admin': reverse('admin:index', request=request, format=format),
        'swagger-ui': reverse('swagger-ui', request=request, format=format),
    })
