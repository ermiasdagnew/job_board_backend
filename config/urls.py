from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ----------------------------
# Swagger / API documentation
# ----------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Job Board API",
        default_version="v1",
        description="API documentation for Job Board",
        contact=openapi.Contact(email="support@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ----------------------------
# Minimal landing page view
# ----------------------------
def home(request):
    return HttpResponse("Job Board API is running!")

# ----------------------------
# URL Patterns
# ----------------------------
urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Landing page
    path("", home, name="home"),

    # API endpoints
    path("api/auth/", include("apps.jobs.urls_auth")),  # Auth routes: register / token
    path("api/jobs/", include("apps.jobs.urls_jobs")),  # Jobs routes
    path("api/applications/", include("apps.jobs.urls_applications")),  # Applications routes

    # Swagger / Redoc
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
