from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms import SignInForm, SignUpForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            print("epic fail")

    return render(request, 'users/signup.html', context={
        'form': SignUpForm(),
    })

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            return redirect('{% user_page', {'username': form.data['username %}']})
    return render(request, 'users/signin.html', context={
        'form': SignInForm(),
    })

def userpage(request, username):
    return render(request, 'users/userpage.html')
