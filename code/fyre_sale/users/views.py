from django.shortcuts import render
from users.forms import SignInForm

# Create your views here.

def sign_up(request):
    return render(request, 'users/signup.html')

def sign_in(request):
    form = SignInForm()

    return render(request, 'users/signin.html', context={
        'form': form,
    })

