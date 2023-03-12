from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.http import HttpResponseNotFound
from django.views.static import serve
from developer_profile.models import DeveloperProfile
from developer_profile.api.serializers import DeveloperProfileSerializer

class DeveloperProfileViewSet(ModelViewSet):
    queryset = DeveloperProfile.objects.all()
    serializer_class = DeveloperProfileSerializer
    
    def media_serve(self, request, path):
        """
        Maneja las solicitudes HTTP de los archivos multimedia y los sirve en la ruta "/media/".
        """
        try:
            # Concatena la ruta de la carpeta media con el path solicitado
            # y utiliza la vista serve de Django para servir el archivo.
            return serve(request, path, document_root=settings.MEDIA_ROOT)
        except Http404:
            # Si el archivo no se encuentra en la carpeta media, devuelve un error 404.
            return HttpResponseNotFound()
            
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == 200 and 'media' in instance.profile_picture.name:
            path = instance.profile_picture.path[len(settings.MEDIA_ROOT):]
            response = self.media_serve(request, path)
        return response
