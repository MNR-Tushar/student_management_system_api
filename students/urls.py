
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management System API",
        default_version='v1',
        description="A comprehensive API for managing educational institution data",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@studentmanagement.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('users/', include('users.urls')),
    path('departments/', include('departments.urls')),
    path('courses/', include('courses.urls')),
    path('teachers/', include('teachers.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('enrollments/', include('enrollments.urls')),
    
    # Swagger URLs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
