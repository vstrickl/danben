from django.urls import path

from . import views

urlpatterns = [
    path("", views.resume, name="resume"),
    path("upload_skills", views.upload_skills, name="upload_skills"),
]