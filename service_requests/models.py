from django.db import models
from django.conf import settings
import uuid

class ServiceRequestCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('billing', 'Billing Inquiry'),
        ('meter', 'Meter Reading'),
        ('repair', 'Repair Request'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    files = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=50, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_number} - {self.title}"