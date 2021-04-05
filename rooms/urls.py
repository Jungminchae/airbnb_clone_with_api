from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ListRoomsView, SeeRoomView


app_name = "rooms"


urlpatterns = [
    path("list/", ListRoomsView.as_view()),
    path("<int:pk>/", SeeRoomView.as_view()),
]
