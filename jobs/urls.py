from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet
router = DefaultRouter()
router.register(r'',JobViewSet, basename='job')
router.register(r'',ApplicationViewSet, basename='application')
urlpatterns = router.urls