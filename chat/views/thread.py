from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chat.models import Thread
from chat.serializers.thread import ThreadSerializer


class ThreadViewSet(ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return super().get_queryset().filter(participants=self.request.user)