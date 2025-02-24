from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from chat.models import Thread
from chat.serializers.thread import ThreadSerializer


class ThreadViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id') or self.request.user.id
        return super().get_queryset().filter(participants__id=user_id)

