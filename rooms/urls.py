from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SeeRoomView, RoomView


app_name = "rooms"


urlpatterns = [
    path("", RoomView.as_view()),
    path("<int:pk>/", SeeRoomView.as_view()),
]
