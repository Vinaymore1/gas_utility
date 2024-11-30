from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceRequest, ServiceRequestCategory
from .serializers import ServiceRequestSerializer, ServiceRequestCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from accounts.permissions import IsAdminUser, IsStaffUser, IsCustomerUser

class ServiceRequestCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for service request categories
    """
    queryset = ServiceRequestCategory.objects.all()
    serializer_class = ServiceRequestCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing service requests with advanced features
    """
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create']:
            permission_classes = [IsCustomerUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return ServiceRequest.objects.all()
        elif user.user_type == 'staff':
            return ServiceRequest.objects.filter(status='open')
        return ServiceRequest.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

# Post-save signal for notifications (notifications/signals.py)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from service_requests.models import ServiceRequest

@receiver(post_save, sender=ServiceRequest)
def send_service_request_notification(sender, instance, created, **kwargs):
    """
    Send email notifications for service request status changes
    """
    if created:
        # Notification for new service request
        send_mail(
            f'New Service Request: {instance.title}',
            f'A new service request has been created. Status: {instance.status}',
            'noreply@gasutility.com',
            [instance.customer.email],
            fail_silently=True
        )
    elif 'status' in kwargs.get('update_fields', []):
        # Notification for status update
        send_mail(
            f'Service Request Update: {instance.title}',
            f'Your service request status has been updated to: {instance.status}',
            'noreply@gasutility.com',
            [instance.customer.email],
            fail_silently=True
        )