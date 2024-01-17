from django.urls import path

from . import views

urlpatterns = [
    path("", views.resume, name="resume"),
    path("preview", views.resume_export, name="resume_export"),
    path("upload_skills", views.upload_skills, name="upload_skills"),
]