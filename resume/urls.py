from django.urls import path

from . import views

urlpatterns = [
    path("", views.resume, name="resume"),
    path("preview", views.resume_export, name="preview"),
    path("upload_skills", views.upload_skills, name="upload_skills"),
    path("download", views.download_resume_pdf, name="download"),
]