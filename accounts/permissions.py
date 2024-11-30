from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'admin'

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type in ['staff', 'admin']

class IsCustomerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'customer'