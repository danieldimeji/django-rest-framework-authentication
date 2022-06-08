from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST API BASE ENDPOINT
    path('api/v1/auth/', include('authentication.urls')),
]
