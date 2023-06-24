from django import forms

class newForm(forms.Form):
    mssv = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    date = forms.CharField(max_length=200)
