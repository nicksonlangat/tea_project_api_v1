from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from accounts.models import Employee
from .serializers import EmployeeSerializer,UserRegisterSerializer, UserSerializer
# Create your views here.

class RegisterUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer


class UserViewset(ListModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('team_leader__email','employee_number')

    def get_queryset(self):
        """
        unless they are admins, team leaders to see only employees assigned to them
        """
        if self.request.user.is_superuser:
            qs = self.queryset
        else:
            qs = self.queryset.filter(team_leader=self.request.user)
        return qs


