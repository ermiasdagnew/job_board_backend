# apps/jobs/apps.py
from django.apps import AppConfig  # <- remove the space

class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.jobs"
    label = "jobs"  # optional, can leave it if you want
