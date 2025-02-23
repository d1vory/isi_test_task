from rest_framework.serializers import ModelSerializer

from chat.models import Thread


class ThreadSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'