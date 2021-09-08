"""Urls V1 API"""

from django.urls import path, include
from rest_framework import routers

# Modules
from .views import hello_data, ProductViewSet, BillViewSet

router = routers.DefaultRouter()


urlpatterns = [
    path("hello", hello_data),
    path("", include(router.urls))
]
