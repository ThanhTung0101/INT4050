from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet

router = DefaultRouter()
router.register(r"comment", CommentViewSet, basename="comment")
urlpatterns = router.urls
