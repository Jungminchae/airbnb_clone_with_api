from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room

# 이것은 매직
class ReadRoomSerializer(serializers.ModelSerializer):
    """
    Serializer => python 객체에서 json 객체로 바꿔 주는 것
    """

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)


# This is 수동
class WriteRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ("user", "modified", "created")

    def validate(self, data):
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")
        return data
