from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('', views.api_root),

    # models
    #path('users/', views.UserList.as_view(), name='user-list'),
    path('profile/<int:pk>', views.profileDetail.as_view(), name='profile-detail'),
    path('user/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('service/comments/', views.CommentList.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('service/jobsites/', views.JobSiteList.as_view()),
    path('service/orders', views.OrderSequenceList.as_view(), name='sequence-list'),
    path('service/order/sequence/<int:pk>', views.OrderSequenceDetail.as_view(), name='sequence-detail'),
    path('service/order/addendum/<int:pk>', views.OrderAddendumDetail.as_view(), name='addendum-detail'),
    path('service/order/item/<int:pk>', views.ItemDetail.as_view(), name='item-detail'),
    path('service/schedules/', views.ScheduleList.as_view(), name='schedule-list'),
    path('service/schedule/<int:pk>', views.ScheduleDetail.as_view(), name='schedule-detail'),
    path('service/centers/', views.ServiceCenterList.as_view()),
    path('service/techs/', views.TechnicianList.as_view()),
    # OpenAPI Reference Definitions Download
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
