from django import forms

class PincodeForm(forms.Form):
    pincode = forms.CharField(label='Enter Pincode', max_length=10)
