from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Job, Region, District
from .serializers import JobSerializer, RegionSerializer, DistrictSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = None

    def get_permissions(self):
        if self.action == 'create':
            # ISH BERISH - Anonymous users ham qila olsin
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Yangilash/o'chirish - Faqat authenticated users
            permission_classes = [IsAuthenticated]
        else:
            # GET - Barchasi qila olsin
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = None
    permission_classes = [AllowAny]


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = None
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def districts_by_region(request):
    region_id = request.query_params.get('region_id')
    if not region_id:
        return Response({'error': 'region_id required'}, status=status.HTTP_400_BAD_REQUEST)

    districts = District.objects.filter(region_id=region_id)
    serializer = DistrictSerializer(districts, many=True)
    return Response(serializer.data)