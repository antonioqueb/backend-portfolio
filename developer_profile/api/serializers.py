from rest_framework.serializers import ModelSerializer
from developer_profile.models import DeveloperProfile

class DeveloperProfileSerializer(ModelSerializer):
    class Meta:
        model = DeveloperProfile
        fields = '__all__'