from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationform(forms.Form):
    user_name = forms.CharField(max_length=20)
    email_id = forms.EmailField(max_length=30)
    pswd = forms.HiddenInput()
    c_pswd = forms.HiddenInput()
    check2 = forms.CheckboxInput()

    def save(self):
        pass


class UserLoginform(forms.Form):
    l_username = forms.CharField(max_length=20)
    l_pswd = forms.HiddenInput()
    check1 = forms.CheckboxInput()