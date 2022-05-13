from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import Payment_info, Address_info, User_info, User_rating
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User

CREDITC_REG = r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\d{11})$'

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
        fields = [
            'card_nr', 'expires', 'cvc'
        ]
        widgets = {
            'card_nr': widgets.TextInput(attrs={'class': 'form-field', 'maxlength': 16, 'pattern': '[0-9]+'}),
            'expires': widgets.TextInput(attrs={'class': 'form-field',
                                                'placeholder': 'MM/YY',
                                                'min_length': 4,
                                                'max_length': 4,
                                                'pattern': '^(0[1-9]|1[0-2])\/?([0-9]{2})$'
}),
            # 'expires': widgets.DateTimeInput(attrs={
            #     'class': 'form-field',
            #     'type': 'date',
            #     'placeholder': 'MM/YY'},
            #     format='%m%Y'),
            'cvc': widgets.TextInput(attrs={'class': 'form-field', 'min_length': 3, 'max_length': 4, 'pattern': '[0-9]+'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(PaymentInsert, self).__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         field.field.widget.attrs['class'] = 'form-field'

class AddressInsert(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AddressInsert, self).__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         field.field.widget.attrs['class'] = 'form-field'

    class Meta:
        model = Address_info
        exclude = ['id']
        widgets = {
            'street_name': widgets.TextInput(attrs={'class': 'form-field'}),
            'zip': widgets.TextInput(attrs={'class': 'form-field'}),
            'city': widgets.TextInput(attrs={'class': 'form-field'}),
            'country': widgets.TextInput(attrs={'class': 'form-field'})
        }

class RateSeller(ModelForm):
    class Meta:
        rates = [(i, i) for i in range(11)]
        model = User_rating
        fields =['user_rating']
        widgets = {
            'user_rating': widgets.Select(attrs={'class': 'form-field'}, choices=rates),
        }

    def __init__(self, *args, **kwargs):
        super(RateSeller, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

class EditUser(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(EditUser, self).__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         field.field.widget.attrs['class'] = 'form-field'

    class Meta:
        model = User_info
        exclude = ['id']
        widgets = {
            'profileimg': widgets.FileInput(attrs={'class': 'form-field'}),
            'bio': widgets.Textarea(attrs={'class': 'form-field', 'type': 'date'}),
            'birthday': widgets.DateTimeInput(attrs={'class': 'form-field', 'type': 'date'}),
        }

class EditAuthUser(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditAuthUser, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email'
        ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-field'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-field'}),
            'email': widgets.DateTimeInput(attrs={'class': 'form-field'}),
        }
