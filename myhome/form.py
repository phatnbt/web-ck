from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class newForm(forms.Form):
    ms = forms.CharField(max_length=100)
    name= forms.CharField(max_length=200)
    price = forms.FloatField()
    image = forms.ImageField()
    description = forms.CharField(max_length=200)
    number = forms.IntegerField()
    # def check(self):
    #     if self.cleaned_price.get('price') <= 0:
    #         raise forms.ValidationError('Giá không hợp lệ')
    #     if self.cleaned_number.get('number') < 0:
    #         raise forms.ValidationError('Số lượng không hợp lệ')
    #     return self.cleaned_data

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

class dangKi(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(label = 'Mật Khẩu', widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Xác nhận mật Khẩu', widget = forms.PasswordInput())
    phonenumber = forms.CharField(label = 'Số điện thoại', max_length=12)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Mật khẩu không khớp!') 
    def save(self):
        CustomUser.objects.create_user(
             username=self.cleaned_data['username'],
             email=self.cleaned_data['email'],
             password=self.cleaned_data['password1']
        )
