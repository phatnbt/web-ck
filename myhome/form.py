from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class newForm(forms.Form):
    mssv = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    date = forms.CharField(max_length=200)


class CustomUserCreationForm (UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('sex_choice', )
        fields = UserCreationForm.Meta.fields + ('age', )
        fields = UserCreationForm.Meta.fields + ('sex', )
        fields = UserCreationForm.Meta.fields + ('address', )
class CustomUserChangeForm (UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
