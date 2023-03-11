from rest_framework.routers import DefaultRouter
from developer_profile.api.views import DeveloperProfileViewSet

router = DefaultRouter()
router.register(r'developer_profile', DeveloperProfileViewSet, basename='developer_profile')