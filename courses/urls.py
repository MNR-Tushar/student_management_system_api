from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'courses', CoursesViewset, basename='course')

urlpatterns = [
    path("", include(router.urls)),
]