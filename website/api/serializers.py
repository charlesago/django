from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from website.models import Message, User, Category


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'



