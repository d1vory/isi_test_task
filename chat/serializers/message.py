from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from chat.models import Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'thread', 'text', 'is_read', 'created')