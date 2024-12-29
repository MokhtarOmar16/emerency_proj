from rest_framework import generics, permissions
from ..models import Emergency
from .serializers import (
    MinimalEmergencySerializer,
    EmergencyDetailSerializer,
    CreateEmergencySerializer,
)
from ..schema import emergency_create_schema

class EmergencyListView(generics.ListAPIView):
    """
    GET /emergencies/
    Returns a minimal list of Emergency objects:
      - id
      - emergency_type
      - description
      - first image (if any)
    """
    queryset = Emergency.objects.all()
    serializer_class = MinimalEmergencySerializer
    permission_classes = [permissions.IsAuthenticated]  # Lock it down if needed


class EmergencyDetailView(generics.RetrieveAPIView):
    """
    GET /emergencies/<pk>/
    Returns a detailed view of a single Emergency:
      - all images
      - user_first_name, user_last_name
      - lat, lgt, etc.
    """
    queryset = Emergency.objects.all()
    serializer_class = EmergencyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]  # Lock it down if needed


@emergency_create_schema
class EmergencyCreateView(generics.CreateAPIView):
    """
    POST /emergencies/create/
    Create a new Emergency record (with up to 5 images).
    The 'user' is automatically set to the requesting user.
    """
    queryset = Emergency.objects.all()
    serializer_class = CreateEmergencySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Attach the current authenticated user
        serializer.save(user=self.request.user)
