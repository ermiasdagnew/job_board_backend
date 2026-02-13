# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ----------------------------
# Root / Home View
# ----------------------------
def home(request):
    return JsonResponse({
        "message": "🚀 Job Board Backend is running!",
        "api_root": "/api/jobs/",
        "docs": "/swagger/"
    })

# ----------------------------
# Swagger/OpenAPI Setup
# ----------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Job Board API",
        default_version="v1",
        description="API documentation for Job Board Backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ----------------------------
# URL Patterns
# ----------------------------
urlpatterns = [
    path("", home, name="home"),  # Root URL
    path("admin/", admin.site.urls),
    path("api/jobs/", include("apps.jobs.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
