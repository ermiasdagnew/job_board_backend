from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView  # 👈 ADD THIS

urlpatterns = [
    # ✅ Register
    path("register/", RegisterView.as_view(), name="register"),

    # ✅ JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
