from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'confirm_password', 
            'first_name', 'last_name', 'phone_number', 'address', 'user_type'
        ]
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'user_type']
        read_only_fields = ['id', 'username', 'email', 'user_type']