from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('sign-up/', views.SignUpAPIView.as_view(), name="sign-up"),
    path('log-in/', views.LogInAPIView.as_view(), name='log-in'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current-user/', views.CurrentUserView.as_view(), name='get-current-user'),
]