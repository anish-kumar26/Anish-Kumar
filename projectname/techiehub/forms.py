# shop/forms.py
from django import forms

class BuyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)
    mobile_number = forms.CharField(max_length=15)
