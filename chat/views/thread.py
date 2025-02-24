from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from chat.models import Thread
from chat.serializers.thread import ThreadSerializer, ThreadListSerializer


class ThreadViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Thread.objects.all()
    list_serializer_class = ThreadListSerializer
    serializer_class = ThreadSerializer
    retrieve_serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return self.serializer_class

    def get_queryset(self):
        return super().get_queryset().filter(participants=self.request.user)

