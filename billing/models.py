from django.db import models
from django.conf import settings

class Account(models.Model):
    """
    Customer billing account
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Account {self.account_number}"

class Bill(models.Model):
    """
    Individual billing records
    """
    BILL_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    )

    account = models.ForeignKey(Account, related_name='bills', on_delete=models.CASCADE)
    billing_period = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=BILL_STATUS_CHOICES, default='pending')
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Bill for {self.account.account_number} - {self.billing_period}"