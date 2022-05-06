from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignInForm(AuthenticationForm):
    def __init__(self):
        super(SignInForm, self).__init__()
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'username', 'first_name', 'last_name', 'password',
        ]

    def __init__(self):
        super(ModelForm, self).__init__()
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'
