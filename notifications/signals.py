from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from service_requests.models import ServiceRequest

@receiver(post_save, sender=ServiceRequest)
def send_service_request_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            f'New Service Request: {instance.title}',
            f'A new service request has been created. Status: {instance.status}',
            'noreply@gasutility.com',
            [instance.customer.email],
            fail_silently=True
        )
    elif 'status' in kwargs.get('update_fields', []):
        send_mail(
            f'Service Request Update: {instance.title}',
            f'Your service request status has been updated to: {instance.status}',
            'noreply@gasutility.com',
            [instance.customer.email],
            fail_silently=True
        )