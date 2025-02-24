from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from chat.models import Thread


class ThreadSerializer(ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    unread_messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = ('id', 'created', 'updated', 'participants', 'unread_messages_count')
        read_only_fields = ('id', 'created', 'updated', 'unread_messages_count')

    def get_unread_messages_count(self, instance: Thread):
        return instance.messages.filter(is_read=False).count()

    def validate_participants(self, value: list[User]):
        user = self.context['request'].user
        if user not in value:
            value.append(user)
        if len(value) > 2:
            raise ValidationError('Thread cannot contain more than 2 people')
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