from django.urls import path
from .views import (
    FileListView,
    HandlePublicText,
    HandlePrivateText,
    HandlePublicFiles,
    HandlePrivateFiles,
)

urlpatterns = [
    path("share-file/", FileListView.as_view(), name="file-list"),
    path("share/public-text/", HandlePublicText.as_view(), name="public-text"),
    path(
        "share/private-text/<int:id>/",
        HandlePrivateText.as_view(),
        name="private-text-detail",
    ),
    path("share/private-text/", HandlePrivateText.as_view(), name="private-text"),
    path("share/public-files/", HandlePublicFiles.as_view(), name="public-files"),
    path("share/private-files/", HandlePrivateFiles.as_view(), name="private-files"),
    path(
        "share/private-files/<int:id>/",
        HandlePrivateFiles.as_view(),
        name="private-files-detail",
    ),
    path("", FileListView.as_view(), name="home"),
]
