from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# ==========================================
# Custom User Model
# ==========================================
class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("USER", "User"),
        ("CANDIDATE", "Candidate"),
    )


    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="USER",
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Avoid clashes with default auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="jobs_user_set",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="jobs_user_permissions_set",
        blank=True,
    )

    def __str__(self):
        return self.username


# ==========================================
# Category Model
# ==========================================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# ==========================================
# Job Model
# ==========================================
class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("FULL_TIME", "Full Time"),
        ("PART_TIME", "Part Time"),
        ("REMOTE", "Remote"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, db_index=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="jobs",
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posted_jobs",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# ==========================================
# Application Model
# ==========================================
class Application(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "job")
        ordering = ["-applied_at"]

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"
