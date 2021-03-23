from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer => python 객체에서 json 객체로 바꿔 주는 것
    """

    class Meta:
        model = Room
        fields = ("name", "price", "instant_book", "user")
