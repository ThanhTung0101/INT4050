from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r"comment", CommentViewSet, basename="comment")
router.register(r"like", LikeViewSet, basename="like")
urlpatterns = router.urls
