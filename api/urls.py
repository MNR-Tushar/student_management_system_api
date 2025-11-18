from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .models import *
from .serializers import *
from .views import *

router = DefaultRouter()
router.register(r'students', StudentsViewset, basename='student')
router.register(r'department', DepartmentViewset, basename='department')
router.register(r'courses', CoursesViewset, basename='course')
router.register(r'teachers', TeachersViewset, basename='teacher')
router.register(r'enrollments', EnrollmentsViewset, basename='enrollment')

urlpatterns = [
    path("", include(router.urls)),
]