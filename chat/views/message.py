from xmlrpc.client import Fault

from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.models import Message
from chat.serializers.message import MessageSerializer


class MessageViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return super().get_queryset().filter(thread_id=self.kwargs['thread_pk'])

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, thread_id=self.kwargs['thread_pk'])

    @action(methods=['post'], detail=True)
    def mark_as_read(self, request, *args, **kwargs):
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response('ok')
