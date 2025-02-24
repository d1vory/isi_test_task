from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from accounts.serializers.user import UserSerializer
from chat.models import Thread
from chat.serializers.message import MessageSerializer


class ThreadListSerializer(ModelSerializer):

    class Meta:
        model = Thread
        fields = ('id', 'created', 'updated', )


class ThreadSerializer(ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'created', 'updated', 'participants', 'messages')
        read_only_fields = ('id', 'created', 'updated', 'messages')


    def validate_participants(self, value: list[User]):
        user = self.context['request'].user
        if user not in value:
            value.append(user)
        if len(value) > 2:
            raise ValidationError('Thread cannot contain more than 2 persons')
        return value

    def create(self, validated_data):
        participants: list[User] = validated_data.get('participants', [])
        existing_thread = Thread.objects.filter(
            participants__in=participants
        ).annotate(
            num_p=Count('participants')
        ).filter(
            num_p=len(participants)
        ).first()
        if existing_thread:
            return existing_thread
        return super().create(validated_data)