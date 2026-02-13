from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobViewSet, CategoryViewSet, ApplicationViewSet, RegisterView

router = DefaultRouter()
router.register("jobs", JobViewSet)
router.register("categories", CategoryViewSet)
router.register("applications", ApplicationViewSet)

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("", include(router.urls)),
]
