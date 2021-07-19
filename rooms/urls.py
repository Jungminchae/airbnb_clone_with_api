from rest_framework.routers import DefaultRouter
import views


app_name = "rooms"
router = DefaultRouter()
router.register("", views.RoomViewSet)

urlpatterns = router.urls
