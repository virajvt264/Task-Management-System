from .views import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
urlpatterns = router.urls
