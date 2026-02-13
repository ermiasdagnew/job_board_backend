from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Job, Application

User = get_user_model()


# ==========================
# User Registration
# ==========================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]

    def create(self, validated_data):
        # Remove role before calling create_user
        role = validated_data.pop("role", "USER")

        # Create user properly (hashes password)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        # Set role separately
        user.role = role
        user.save()

        return user


# ==========================
# Category
# ==========================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# ==========================
# Job
# ==========================
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


# ==========================
# Application
# ==========================
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ["user", "applied_at"]
