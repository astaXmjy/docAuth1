from django.contrib import admin
from django.urls import path
from .views import extract

urlpatterns = [
    path("upload/", extract, name="upload"),
]
