from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import UserSerializer


class UserPagination(PageNumberPagination):
    """Users pagination - 10 ta sahifada"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserViewSet(viewsets.ModelViewSet):
    """
    User ViewSet - faqat admin panel/ichki boshqaruv uchun.

    Saytda ochiq ro'yxatdan o'tish yo'q, shuning uchun bu API'ga
    faqat login qilgan admin (staff) foydalanuvchilar kira oladi.

    GET /api/users/ - Barcha users (faqat admin)
    POST /api/users/ - Yangi user qo'shish (faqat admin)
    GET /api/users/{id}/ - Single user (faqat admin)
    PUT/PATCH /api/users/{id}/ - Update user (faqat admin)
    DELETE /api/users/{id}/ - Delete user (faqat admin)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
