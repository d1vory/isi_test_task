from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.serializers.user import UserSerializer
from chat.models import Message


class MessageSerializer(ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'thread', 'text', 'is_read', 'created')
        read_only_fields = ('id', 'sender', 'thread', 'is_read', 'created')