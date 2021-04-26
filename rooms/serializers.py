from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room

# 이것은 매직
class ReadRoomSerializer(serializers.ModelSerializer):
    """
    Serializer => python 객체에서 json 객체로 바꿔 주는 것
    """

    user = UserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)


# This is 수동
class WriteRoomSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    beds = serializers.IntegerField()
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def validate_beds(self, beds):
        if beds < 5:
            raise serializers.ValidationError("Your house is too small")
        else:
            return beds