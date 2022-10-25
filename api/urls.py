from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from api import views

urlpatterns = [
    # models
    path('service/comments/', views.CommentList.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('service/jobsites/', views.JobSiteList.as_view()),
    path('service/order/sequence/', views.OrderSequenceList.as_view()),
    path('service/order/addendum/', views.OrderAddendumList.as_view()),
    path('service/order/<int:pk>/', views.OrderAddendumDetail.as_view()),
    path('service/order/items/', views.ItemList.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('service/Schedules/', views.ScheduleList.as_view()),
    path('service/centers/', views.ServiceCenterList.as_view()),
    path('service/techs/', views.TechnicianList.as_view()),
    # Swagger Reference Definitions Download
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)