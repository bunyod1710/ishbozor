from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # SWAGGER
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # API
    path('api/users/', include('users.urls')),
    path('api/', include('jobs.urls')),

    # FRONTEND PAGES
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('ish-berish/', TemplateView.as_view(template_name='ish-berish.html'), name='ish-berish'),
    path('jobs/', TemplateView.as_view(template_name='jobs.html'), name='jobs'),
    path('ishlarni-korish/', TemplateView.as_view(template_name='ishlarni-korish.html'), name='ishlarni-korish'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
]