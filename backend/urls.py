from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# API imports
from developer_profile.api.router import router as developer_profile_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(developer_profile_router.urls)),
]

# Servir archivos estáticos en producción
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
