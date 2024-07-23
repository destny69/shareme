from django.urls import path

from .views import *

urlpatterns = [
    path("share-file/", FileListView.as_view()),
    path("share/public-text/", HandlePublicText.as_view()),
    path("share/private-text/<id>/", HandlePrivateText.as_view()),
    path("share/private-text/", HandlePrivateText.as_view()),
    path("share/public-files/", HandlePublicFiles.as_view()),
    path("share/private-files/", HandlePrivateFiles.as_view()),
    path("", FileListView.as_view()),
]
