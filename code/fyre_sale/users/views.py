from django.shortcuts import render
from users.forms import SignInForm, SignUpForm

# Create your views here.

def sign_up(request):
    return render(request, 'users/signup.html', context={
        'form': SignUpForm(),
    })

def sign_in(request):
    return render(request, 'users/signin.html', context={
        'form': SignInForm(),
    })

def userpage(request, userid):
    return render(request, 'users/userpage.html')
