from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import JobViewSet, ApplicationViewSet, jobs_list

router = DefaultRouter()
router.register(r'', JobViewSet, basename='job')
router.register(r'', ApplicationViewSet, basename='application')

urlpatterns = [
    path('list/', jobs_list, name='jobs_list'),  # Template view
] + router.urls