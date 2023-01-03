from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from api import views

urlpatterns = [
    # Auth
    path('auth/login', views.LoginView.as_view()),
    path('auth/logout', views.LogoutView.as_view()),
    
    # User Models
    path('user/profile', views.ProfileDetail.as_view(), name='profile'),

    # Generic Models
    path('generic/customers', views.CustomerList.as_view()),
    path('generic/customer/<int:pk>', views.CustomerDetail.as_view()),
    path('generic/regions', views.RegionList.as_view()),
    path('generic/cities', views.CityList.as_view()),
    path('generic/zipcodes', views.ZipCodeList.as_view()),

    # Service Models
    path('service/comments', views.CommentList.as_view()),
    path('service/comment/<int:pk>', views.CommentDetail.as_view()),
    path('service/jobsites', views.JobSiteList.as_view()),
    path('service/jobsite/<int:pk>', views.JobSiteDetail.as_view()),
    path('service/orders/sequences', views.OrderSequenceList.as_view(), name='sequence-list'),
    path('service/order/sequence/<int:pk>', views.OrderSequenceDetail.as_view(), name='sequence-detail'),
    path('service/order/addendums', views.OrderAddendumList.as_view(), name='addendum-list'),
    path('service/order/addendum/<int:pk>', views.OrderAddendumDetail.as_view(), name='addendum-detail'),
    path('service/order/item/<int:pk>', views.ItemDetail.as_view(), name='item-detail'),
    path('service/schedules', views.ScheduleList.as_view(), name='schedule-list'),
    path('service/schedule/<int:pk>', views.ScheduleDetail.as_view(), name='schedule-detail'),
    path('service/centers', views.ServiceCenterList.as_view()),
    path('service/center/<int:pk>', views.ServiceCenterDetail.as_view()),
    path('service/techs', views.TechnicianList.as_view()),
    path('service/tech/<int:pk>', views.TechnicianDetail.as_view()),
    path('service/managers', views.ManagerList.as_view()),

    # OpenAPI Reference Definitions Download
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
