from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer => python 객체에서 json 객체로 바꿔 주는 것
    """

    user = UserSerializer()

    class Meta:
        model = Room
        fields = ("pk", "name", "price", "user")
