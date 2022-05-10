from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import Payment_info, Address_info
from django.forms import ModelForm, widgets
from django.forms.utils import ErrorList

# class DivErrorList(ErrorList):
#     def __str__(self):
#         return self.as_divs()
#
#     def as_divs(self):
#         if not self: return ''
#         return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])
#         f = AddressInsert(data, auto_id=False, error_class=DivErrorList)
#         f.as_p()
#
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
        exp = '%m-%Y'
        exclude = ['id']
        widgets = {
            'card_nr': widgets.TextInput(attrs={'class': 'form-field', 'maxlength': 16, 'pattern': '[0-9]+'}),
            'expires': widgets.DateTimeInput(attrs={
                'class': 'form-field',
                'type': 'date',
                'placeholder': 'MM/YY'},
                format='%m/%Y'),
            'cvc': widgets.TextInput(attrs={'class': 'form-field', 'size': '20', 'minlength': 3, 'maxlength': 4})
        }
    # def __init__(self, *args, **kwargs):
    #     super(PaymentInsert, self).__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         if field.name == 'card_nr':
    #             'card_nr': widgets.NumberInput()
    #         field.field.widget.attrs['class'] = 'form-field'

class AddressInsert(ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super(AddressInsert, self).__init__(*args, **kwargs)
            for field in self.visible_fields():
                field.field.widget.attrs['class'] = 'form-field'
        model = Address_info
        exclude = ['id']
        widgets = {
            'street_name': widgets.TextInput(attrs={'class': 'form-field'}),
            'zip': widgets.TextInput(attrs={'class': 'form-field'}),
            'city': widgets.TextInput(attrs={'class': 'form-field'}),
            'country': widgets.TextInput(attrs={'class': 'form-field'})
        }