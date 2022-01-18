from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import TeaWeight
from core.serializers import TeaWeightSerializer

# Create your views here.
class TeaWeightViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TeaWeight.objects.all()
    serializer_class = TeaWeightSerializer
    filter_backends = (filters.DjangoFilterBackend,)

