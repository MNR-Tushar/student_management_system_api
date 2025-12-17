from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'teachers', TeachersViewset, basename='teacher')


urlpatterns = [
    path("", include(router.urls)),
] 