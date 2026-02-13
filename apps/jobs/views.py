from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Category, Application, User
from .serializers import JobSerializer, CategorySerializer, ApplicationSerializer, RegisterSerializer
from .permissions import IsAdmin, IsUser

# -------------------
# User Registration
# -------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# -------------------
# Jobs
# -------------------
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location", "job_type", "category"]

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsAdmin()]
        return [AllowAny()]


# -------------------
# Categories
# -------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsAdmin()]
        return [AllowAny()]


# -------------------
# Applications
# -------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
