from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Room
from .serializers import RoomSerializer


# django view가 아니라 api가 작동하게 하기 위해서 필요
# @api_view(["GET", "POST"])
# def rooms_view(request):
#     if request.method == "GET":
#         rooms = Room.objects.all()
#         serializer = ReadRoomSerializer(rooms, many=True).data
#         return Response(serializer)
#     elif request.method == "POST":
#         # POST => Create
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         serializer = WriteRoomSerializer(data=request.data)
#         if serializer.is_valid():
#             room = serializer.save(user=request.user)
#             room_serializer = ReadRoomSerializer(room).data
#             return Response(data=room_serializer, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnPagination(PageNumberPagination):
    page_size = 20


class RoomsView(APIView):
    def get(self, request):
        paginator = OwnPagination()
        rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializers = RoomSerializer(results, many=True).data
        return paginator.get_paginated_response(serializers)

    def post(self, request):
        # POST => Create
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = RoomSerializer(room).data
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomVeiw(APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_object(pk)
        if room is not None:
            serializer = RoomSerializer(room).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        room = self.get_object(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = RoomSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                room = serializer.save()
                return Response(RoomSerializer(room).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def room_search(request):
    paginator = OwnPagination()
    paginator.page_size = 10
    rooms = Room.objects.filter()
    results = paginator.paginate_queryset(rooms, request)
    serializers = RoomSerializer(results, many=True).data
    return paginator.get_paginated_response(serializers)


# 중요한 rest_framework serializer method
# create, update, save
# 궁금하면 doc를 볼 것

# create method는 직접적으로 call 하면 안됨 -> save를 해 -> save가 create를 call 할 거야