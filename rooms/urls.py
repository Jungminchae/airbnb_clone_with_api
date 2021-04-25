from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SeeRoomView, rooms_view


app_name = "rooms"


urlpatterns = [
    path("", rooms_view),
    path("<int:pk>/", SeeRoomView.as_view()),
]
