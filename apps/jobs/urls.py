# apps/jobs/urls.py
from django.urls import path
from .views import JobListCreateView  # make sure this view exists

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="job-list-create"),
]
