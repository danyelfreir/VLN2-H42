from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'



# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = [
#             'email', 'username', 'first_name', 'last_name', 'password', 'confirm_password',
#         ]
#
#     def __init__(self):
#         super(forms.ModelForm, self).__init__()
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-field'
#
#     def clean_password2(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         print('here')
