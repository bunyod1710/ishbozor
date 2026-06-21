from rest_framework.viewsets import ModelViewSet
from .serializers import JobSerializer, ApplicationSerializer
from .models import Job, Application
class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

