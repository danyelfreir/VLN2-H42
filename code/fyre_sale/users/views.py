from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect,get_object_or_404
from users.forms import SignInForm, SignUpForm, PaymentInsert, AddressInsert, EditUser, EditAuthUser
from users.models import User, Notification, User_info
from items.models import Offer

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'users/userpage.html', context={
        'user': user
    })


def inbox(request, params=None):
    user = User.objects.get(username=request.user)
    if params == 'my_bids':
        offers = Offer.objects.filter(buyer_id=user.id)
        return render(request, 'users/inbox.html', context={
            'user': user,
            'offers': offers
        })
    elif params == 'my_items':
        bids = Offer.objects.raw("\n"
                                 "SELECT * FROM items_offer O WHERE O.item_id IN (\n"
                                 "SELECT I.id FROM items_itemforsale I WHERE I.seller_id = %s);", [user.id])
        return render(request, 'users/inbox.html', context={
            'user': user,
            'bids': bids,
        })
    notifications = Notification.objects.filter(recipient=user)
    return render(request, 'users/inbox.html', context={
        'user': user,
        'notifications': notifications
    })


def notification(request, not_id):
    return render(request, 'users/notification.html', context={
        'not': not_id
    })


def userpage(request, username):
    return render(request, 'users/userpage.html')


def payment(request):
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

def address(request):
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = AddressInsert(request.POST)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
            # user_id.save()
        return redirect('profile')
    else:
        form = AddressInsert()
    return render(request, 'users/address.html', {
        'form': form
    })

def edit_user(request):
    if request.method =='POST':
        instance1 = get_object_or_404(User, username=request.user)
        instance2 = get_object_or_404(User_info, id=request.user.id)
        form1 = EditUser(request.POST, instance=instance2)
        form2 = EditAuthUser(request.POST, instance=instance1)
        if form1.is_valid():
            sendform1 = form1.save(commit=False)
            sendform1.username = instance1
            print(instance1)
            # form1.save()
            sendform1.save()
            print("form1")
        if form2.is_valid():
            sendform2 = form2.save(commit=False)
            sendform2.id_id = instance2.username
            sendform2.save()
            print("form2")
        # if form1.is_valid() and form2.is_valid():
        #     signed_in_user = form2.save(commit=False)
        #     signed_in_auth_user = form1.save(commit=False)
            # signed_in_user.id_id.save()
            # signed_in_auth_user.username.save()
            # form1.save()
            # form2.save()
        return redirect('payment')
    else:
        form1 = EditUser()
        form2 = EditAuthUser()
    return render(request, 'users/edit_user.html', {
        'form1': form1,
        'form2': form2
    })
