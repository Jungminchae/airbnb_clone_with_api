from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    """
    Serializer => python 객체에서 json 객체로 바꿔 주는 것
    """

    name = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    instant_book = serializers.BooleanField()