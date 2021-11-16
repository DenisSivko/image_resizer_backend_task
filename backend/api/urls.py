from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ImageViewSet

router = DefaultRouter()
router.register("images", ImageViewSet, basename="images")

urlpatterns = [
    path("", include(router.urls)),
]
