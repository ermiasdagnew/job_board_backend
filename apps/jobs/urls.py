from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobViewSet, CategoryViewSet, ApplicationViewSet, RegisterView

router = DefaultRouter()
router.register(r"jobs", JobViewSet, basename="jobs")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"applications", ApplicationViewSet, basename="applications")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
]
