from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, ServiceRequestCategoryViewSet

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet, basename='service-request')
router.register(r'service-request-categories', ServiceRequestCategoryViewSet, basename='service-request-category')

urlpatterns = [
    path('', include(router.urls)),
]