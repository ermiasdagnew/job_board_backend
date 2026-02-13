# apps/jobs/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CategoryViewSet, ApplicationViewSet, RegisterView

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r"jobs", JobViewSet, basename="jobs")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"applications", ApplicationViewSet, basename="applications")

# Define URL patterns
urlpatterns = [
    # User registration
    path("auth/register/", RegisterView.as_view(), name="register"),
    
    # Include all router URLs (jobs, categories, applications)
    path("", include(router.urls)),
]
