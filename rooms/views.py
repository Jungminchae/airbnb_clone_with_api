from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer


class ListRoomsView(ListAPIView):
    # 커스터 마이징 할 것이 없을 때 generic view를 쓰면 됨
    queryset = Room.objects.all()  # query set 만들고
    serializer_class = RoomSerializer  # serializer 만들면 끝


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer