from rest_framework.routers import DefaultRouter
from django.urls import path
import rooms.views

app_name = "rooms"

urlpatterns = [
    path("", rooms.views.RoomsView.as_view()),
    path("search/", rooms.views.room_search),
    path("<int:pk>/", rooms.views.RoomVeiw.as_view()),
]
