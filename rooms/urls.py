from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RoomVeiw, RoomsView


app_name = "rooms"


urlpatterns = [
    path("", RoomsView.as_view()),
    path("<int:pk>/", RoomVeiw.as_view()),
]
