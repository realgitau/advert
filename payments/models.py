from django.db import models
from django.utils import timezone
import secrets
from .paystack import PayStack


class Payment(models.Model):
    ref = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    receipt_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        ordering = ['-date_created',]

    
    def __str__(self) -> str:
        return f"KES {self.amount} ---- Receipt:{self.receipt_number} ---- for {self.email}"
    
    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            self.receipt_number = result['receipt_number']
            authorization = result.get('authorization', {})
            self.phone_number = f"{authorization.get('bin', '')}{authorization.get('last4', '')}"
            if result['amount']/100 == self.amount:
                self.verified = True
            self.save()
            return self.verified
        
        else:
            return False
    
