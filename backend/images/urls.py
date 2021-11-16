from django.urls import path

from images.views import (ImageCreateView, ImageDetailView, ImageListView,
                          ImageResizeView)

urlpatterns = [
    path("", ImageListView.as_view(), name="index"),
    path("images/<int:pk>/", ImageDetailView.as_view(), name="image_detail"),
    path("upload/", ImageCreateView.as_view(), name="upload"),
    path("images/<int:pk>/resize/", ImageResizeView.as_view(), name="resize"),
]
