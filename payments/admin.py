from django.contrib import admin
from .models import Payment
from django.utils import timezone

class PaymentAdmin(admin.ModelAdmin):
    def date(self, obj):
        if obj.date_created:
            return timezone.localtime(obj.date_created)
        return None
    
    list_display = ['receipt_number', 'amount', 'phone_number', 'email', 'verified', 'date']

admin.site.register(Payment, PaymentAdmin)

