from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1, max_value=150000, widget=forms.NumberInput(attrs={'placeholder': 'Amount in KES'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Confirm your Email'}))
    class Meta:
        model = Payment
        fields = ["amount", "email"]