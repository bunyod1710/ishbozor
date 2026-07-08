from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, RegionViewSet, DistrictViewSet, districts_by_region

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'regions', RegionViewSet, basename='region')
router.register(r'districts', DistrictViewSet, basename='district')

urlpatterns = [
    path('districts/by_region/', districts_by_region, name='districts_by_region'),
    path('', include(router.urls)),
]