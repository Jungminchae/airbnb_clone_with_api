from django.urls import path
import views

app_name = "users"

urlpatterns = [
    path("me/", views.MeView.as_view()),
    path("<int:pk>/", views.user_detail),
]
