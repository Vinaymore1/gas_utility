from rest_framework import serializers
from .models import Account, Bill

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_number', 'balance', 'is_active']
        read_only_fields = ['id', 'account_number']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = [
            'id', 'account', 'billing_period', 
            'amount_due', 'due_date', 'status', 
            'payment_date'
        ]
        read_only_fields = ['id', 'account']