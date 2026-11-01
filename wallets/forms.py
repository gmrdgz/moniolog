from django import forms


class NewWallet(forms.Form):
    bank_name = forms.CharField(label='Bank name')
    account_code = forms.CharField(label='Account code')
