
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/', include('student_info.urls')),
    path('users/', include('users.urls')),
    path('departments/', include('departments.urls')),
    path('courses/', include('courses.urls')),
    path('teachers/', include('teachers.urls')),
    path('enrollments/', include('enrollments.urls')),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
  
    
]

