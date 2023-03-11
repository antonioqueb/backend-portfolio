from rest_framework.viewsets import ModelViewSet
from developer_profile.models import DeveloperProfile
from developer_profile.api.serializers import DeveloperProfileSerializer

class DeveloperProfileViewSet(ModelViewSet):
    queryset = DeveloperProfile.objects.all()
    serializer_class = DeveloperProfileSerializer