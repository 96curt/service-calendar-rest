from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from api import views

urlpatterns = [
    # Auth
    path('auth/login', views.LoginView.as_view()),
    path('auth/logout', views.LogoutView.as_view()),
    # models
    path('profile/', views.ProfileDetail.as_view(), name='profile'),
    path('service/comments/', views.CommentList.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('service/jobsites/', views.JobSiteList.as_view()),
    path('service/orders/sequences', views.OrderSequenceList.as_view(), name='sequence-list'),
    path('service/order/sequence/<int:pk>', views.OrderSequenceDetail.as_view(), name='sequence-detail'),
    path('service/order/addendums', views.OrderAddendumList.as_view(), name='addendum-list'),
    path('service/order/addendum/<int:pk>', views.OrderAddendumDetail.as_view(), name='addendum-detail'),
    path('service/order/item/<int:pk>', views.ItemDetail.as_view(), name='item-detail'),
    path('service/schedules/', views.ScheduleList.as_view(), name='schedule-list'),
    path('service/schedule/<int:pk>', views.ScheduleDetail.as_view(), name='schedule-detail'),
    path('service/centers/', views.ServiceCenterList.as_view()),
    path('service/techs/', views.TechnicianList.as_view()),
    # OpenAPI Reference Definitions Download
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
