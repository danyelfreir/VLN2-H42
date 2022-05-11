from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from users.forms import SignInForm, SignUpForm, PaymentInsert, AddressInsert, EditUser, EditAuthUser
from users.models import Notification, User_info
from items.models import Offer

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user_info_form = User_info.objects.create(id=new_user)
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', context={
        'form': form,
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
                return redirect('index')
    else:
        form = SignInForm()
    return render(request, 'users/signin.html', context={
        'form': form,
    })


def profilepage(request, username):
    user = User.objects.get(username=username)
    user_info = User_info.objects.get(pk=user.id)
    return render(request, 'users/userpage.html', context={
        'user_profile': user,
        'user_info': user_info
    })


@login_required
def inbox(request, username):
    if username != request.user.username:
        raise Http404()

    offers = Offer.objects.filter(buyer_id=request.user.id)
    bids = Offer.objects.raw("\n"
                             "SELECT * FROM items_offer O WHERE O.item_id IN (\n"
                             "SELECT I.id FROM items_itemforsale I WHERE I.seller_id = %s);", [request.user.id])
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'users/inbox.html', context={
        'offers': offers,
        'bids': bids,
        'notifications': notifications,
    })


@login_required
def notification(request, username, not_id):
    if username != request.user.username:
        raise Http404()

    notification = Notification.objects.get(pk=not_id)
    return render(request, 'users/notification.html', context={
        'notification': notification
    })


@login_required
def payment(request, username):
    if username != request.user.username:
        raise Http404()

    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = PaymentInsert(request.POST)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
            user_id.save()
            return redirect('profile')
    else:
        form = PaymentInsert()
    return render(request, 'users/payment.html', {
        'form': form
    })


@login_required
def address(request, username):
    if username != request.user.username:
        raise Http404()

    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = AddressInsert(request.POST)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
        return redirect('profile')
    else:
        form = AddressInsert()
    return render(request, 'users/address.html', {
        'form': form
    })

def edit_user(request):
    instance1 = get_object_or_404(User_info, pk=request.user.id)
    instance2 = get_object_or_404(User, pk=request.user.id)
    if request.method =='POST':
        form1 = EditUser(data=request.POST, instance=instance1)
        form2 = EditAuthUser(data=request.POST, instance=instance2)
        print(form2.fields)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('payment')
    else:
        form1 = EditUser(instance=instance1)
        form2 = EditAuthUser(instance=instance2)
    return render(request, 'users/edit_user.html', {
        'form1': form1,
        'form2': form2
    })
