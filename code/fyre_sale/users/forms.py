from django.contrib.auth.forms import AuthenticationForm

class SignInForm(AuthenticationForm):
    def __init__(self):
        super(SignInForm, self).__init__()
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

