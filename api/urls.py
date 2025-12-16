from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'students', StudentsViewset, basename='student')
router.register(r'teachers', TeachersViewset, basename='teacher')
router.register(r'enrollments', EnrollmentsViewset, basename='enrollment')

urlpatterns = [
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]