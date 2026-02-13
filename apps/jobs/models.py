# apps/jobs/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model (if you want to extend default fields)
class User(AbstractUser):
    # Add any extra fields here if needed
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


# Job Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Job model
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="jobs")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Job Application model
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default="pending")

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
