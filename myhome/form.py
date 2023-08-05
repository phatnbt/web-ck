from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class newForm(forms.Form):
    ms = forms.CharField(max_length=100)
    name= forms.CharField(max_length=200)
    price = forms.CharField(max_length=200)
    image = forms.ImageField()
    description = forms.CharField(max_length=200)
    number = forms.CharField(max_length=200)


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
