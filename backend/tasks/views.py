from rest_framework import viewsets, permissions
from tasks.serializers import CateforySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CateforySerializer

    def get_queryset(self):
        return self.request.user.categories.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
