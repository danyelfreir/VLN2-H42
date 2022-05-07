from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import SignInForm, SignUpForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            print("epic fail")

    return render(request, 'users/signup.html', context={
        'form': SignUpForm(),
    })

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'users/signin.html', context={
        'form': SignInForm(),
    })

def userpage(request, username):
    return render(request, 'users/userpage.html')
