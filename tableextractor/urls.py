from django.contrib import admin
from django.urls import path
from .views import UploadFileAPIView,GetExtractedTables
urlpatterns = [
    path('upload-pdf',UploadFileAPIView.as_view()),
    path('get-extracted-text/<int:id>',GetExtractedTables.as_view())
]