from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def sign_up(request):
    return render(request, 'modals/signup.html')

def sign_in(request):
    form = AuthenticationForm()
    return render(request, 'users/sign_in.html', context={
        'form': form,
    })

