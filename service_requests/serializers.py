from .models import ServiceRequest, ServiceRequestCategory
from rest_framework import serializers

class ServiceRequestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequestCategory
        fields = ['id', 'name', 'description']

class ServiceRequestSerializer(serializers.ModelSerializer):
    category = ServiceRequestCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequestCategory.objects.all(), 
        source='category', 
        write_only=True
    )
    customer_name = serializers.SerializerMethodField()
    attachment_url = serializers.SerializerMethodField()

    class Meta:
        model = ServiceRequest
        fields = [
            'id', 'customer', 'customer_name', 'category', 'category_id', 
            'title', 'description', 'status', 'priority', 
            'created_at', 'updated_at', 'resolved_at', 
            'attachments', 'attachment_url'
        ]
        read_only_fields = ['customer', 'created_at', 'updated_at', 'resolved_at', 'customer_name']

    def get_customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"

    def get_attachment_url(self, obj):
        if obj.attachments:
            return obj.attachments.url
        return None