from django.contrib.auth import login, authenticate
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from users.models import User_info, Notification
from items.models import Offer, ItemForSale
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from users.models import Notification, User_info, Address_info, Payment_info
from items.models import Offer
from users.forms import SignInForm, SignUpForm, PaymentInsert, AddressInsert, EditUser, EditAuthUser,RateSeller


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
    joined = user.date_joined.strftime("%x")
    print("test")
    print(joined)
    return render(request, 'users/userpage.html', context={
        'user_profile': user,
        'user_info': user_info,
        'joined': joined
    })
@login_required
def inbox(request, username):
    if username != request.user.username:
        raise Http404()

    offers = Offer.objects.filter(buyer_id=request.user.id).order_by('-time_of_offer')
    bids = Offer.objects.raw("\n"
                             "SELECT * FROM items_offer O WHERE O.item_id IN (\n"
                             "SELECT I.id FROM items_itemforsale I WHERE I.seller_id = %s)\n"
                             "ORDER BY O.time_of_offer DESC;", [request.user.id])
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
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
def edit_payment(request, username):
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
def edit_address(request, username):
    if username != request.user.username:
        raise Http404()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = AddressInsert(request.POST)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
        return redirect('profile', username=username)
    else:
        form = AddressInsert()
    return render(request, 'users/address.html', {
        'form': form
    })


def checkout(request, offer_id, step):
    try:
        user_address_instance = Address_info.objects.get(pk=request.user.id)
    except Address_info.DoesNotExist:
        user_address_instance = None
    try:
        user_payment_instance = Payment_info.objects.get(pk=request.user.id)
    except Payment_info.DoesNotExist:
        user_payment_instance = None
    if step == 1:
        if request.method == 'POST':
            form = EditAuthUser(data=request.POST, instance=request.user)
            if form.is_valid():
                if request.POST.get('save-info') == 'yes':
                    form.save()
                else:
                    request.session['user_info'] = form.cleaned_data
                return redirect('checkout', offer_id=offer_id, step=step+1)
        else:
            if 'user_info' in request.session:
                form = EditAuthUser(initial=request.session['user_info'])
            else:
                form = EditAuthUser(instance=request.user)
    elif step == 2:
        if request.method == 'POST':
            form = AddressInsert(data=request.POST, instance=user_address_instance)
            if form.is_valid():
                if request.POST.get('save-info') == 'yes':
                    form.save()
                else:
                    request.session['user_address'] = form.cleaned_data
                return redirect('checkout', offer_id=offer_id, step=step+1)
        else:
            if 'user_address' in request.session:
                form = AddressInsert(initial=request.session['user_address'])
            else:
                form = AddressInsert(instance=user_address_instance)
    elif step == 3:
        if request.method == 'POST':
            form = PaymentInsert(data=request.POST, instance=user_payment_instance)
            if form.is_valid():
                if request.POST.get('save-info') == 'yes':
                    form.save()
                else:
                    request.session['user_payment'] = form.cleaned_data
                    print(request.session.keys())
            else:
                print("No validato :(")
                print(form.errors)
                return redirect('checkout', offer_id=offer_id, step=step)
        else:
            if 'user_payment' in request.session:
                form = PaymentInsert(initial=request.session['user_payment'])
            else:
                form = PaymentInsert(instance=user_payment_instance)

    return render(request, 'users/checkout.html', context={
        'form': form,
        'offer': offer_id,
        'next': step,
        'prev': step - 1,
    })


@login_required
def rate_sales(request, username, not_id):
    if username != request.user.username:
        raise Http404()
    print(request.POST)
    notification = Notification.objects.get(pk=not_id)
    if username != request.user.username:
        raise Http404()
    if request.method == 'POST':
        form = RateSeller(request.POST, notification)
        if form.is_valid():
            form.save()
            return redirect('user_page')
    else:
        form = RateSeller(request.POST)
    return render(request, 'users/rateseller.html', {
        'form': form,
        'username': username,
        'notification': notification,
    })

def edit_profile(request, username):
    if username != request.user.username:
        raise Http404()

    instance1 = get_object_or_404(User_info, pk=request.user.id)
    instance2 = get_object_or_404(User, pk=request.user.id)
    if request.method =='POST':
        form1 = EditUser(data=request.POST, instance=instance1)
        form2 = EditAuthUser(data=request.POST, instance=instance2)
        print(form2.fields)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('profile', username=username)
    else:
        form1 = EditUser(instance=instance1)
        form2 = EditAuthUser(instance=instance2)
    return render(request, 'users/edit_user.html', {
        'form1': form1,
        'form2': form2
    })


def clean_checkout_session(request):
    try:
        del request.session['user_info']
    except KeyError:
        pass
    try:
        del request.session['user_address']
    except KeyError:
        pass
    try:
        del request.session['user_payment']
    except KeyError:
        pass
    print(request.session.keys())
    return HttpResponse("Clean as fuck boi")
