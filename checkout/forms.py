from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    # Month and YEAR Expire
    MONTH_CHOICE = [(i, i) for i in range(1, 12)]
    YEAR_CHOICE = [(i, i) for i in range(2017, 2036)]
    
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICE)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICE, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    