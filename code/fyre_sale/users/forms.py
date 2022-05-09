from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import Payment_info
from django.forms import ModelForm, widgets
class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username", "email", "password1", "password2"
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PaymentInsert(ModelForm):
    class Meta:
        model = Payment_info
        exclude = ['id']
        format = '%m-%Y'
        widgets = {
            'card_nr': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxx-xxxx-xxxx-xxxx'})
            'expires': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'mm/yy'}.format)
        }