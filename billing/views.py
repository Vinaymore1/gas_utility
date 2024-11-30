from rest_framework import viewsets, permissions
from .serializers import AccountSerializer, BillSerializer
from .models import Account, Bill

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

class BillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Bill.objects.filter(account__user=user).order_by('-billing_period')
