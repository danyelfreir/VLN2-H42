from django.core                    import serializers
from django.contrib                 import messages
from django.contrib.auth            import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import UserCreationForm, AuthenticationForm
from django.contrib.auth.models     import User
from django.http                    import Http404, HttpResponse
from django.shortcuts               import render, redirect, get_object_or_404
# from users.forms                    import SignInForm, SignUpForm, PaymentInsert, AddressInsert, EditUser, EditAuthUser,RateSeller
from users.forms                    import *
from users.models                   import User_info, Address_info, Payment_info, Notification, User_rating
from items.models                   import Offer, ItemForSale, SoldItem
from datetime                       import datetime
from django.core.mail               import send_mail

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
    print(user_info)
    joined = user.date_joined.strftime("%x")
    user_rating = calculate_average(user)
    print(joined)
    return render(request, 'users/userpage.html', context={
        'user_profile': user,
        'user_info': user_info,
        'joined': joined,
        'rating': user_rating,
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
    instance = get_object_or_404(Payment_info, pk=request.user.id)
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = PaymentInsert(data=request.POST, instance=instance)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
            user_id.save()
            return redirect('profile', username=username)
    else:
        form = PaymentInsert(instance=instance)
    return render(request, 'users/payment.html', {
        'form': form
    })


@login_required
def edit_address(request, username):
    if username != request.user.username:
        raise Http404()
    instance = get_object_or_404(Address_info, pk=request.user.id)
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = AddressInsert(data=request.POST, instance=instance)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.id_id = tmp_user.id
            user_id.save()
        return redirect('profile', username=username)
    else:
        form = AddressInsert(instance=instance)
    return render(request, 'users/address.html', {
        'form': form
    })


@login_required
def checkout(request, not_id, step):
    # if get_object_or_none(SoldItem, )
    user_address_instance = get_object_or_none(Address_info, request.user.id)
    user_payment_instance = get_object_or_none(Payment_info, request.user.id)

    if step == 1:
        if request.method == 'POST':
            form = EditAuthUser(data=request.POST, instance=request.user)
            if form.is_valid():
                if request.POST.get('save-info') == 'yes':
                    form.save()
                request.session['user_info'] = form.cleaned_data
                return redirect('checkout', not_id=not_id, step=step+1)
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
                    tmp_form = form.save(commit=False)
                    tmp_form.id = request.user
                    tmp_form.save()
                request.session['user_address'] = form.cleaned_data
                return redirect('checkout', not_id=not_id, step=step+1)
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
                    tmp_form = form.save(commit=False)
                    tmp_form.id = request.user
                    tmp_form.save()
                request.session['user_payment'] = form.cleaned_data
            return redirect('checkout_confirm', not_id=not_id)
        else:
            if 'user_payment' in request.session:
                form = PaymentInsert(initial=request.session['user_payment'])
            else:
                form = PaymentInsert(instance=user_payment_instance)

    return render(request, 'users/checkout.html', context={
        'form': form,
        'not_id': not_id,
        'next': step,
    })


@login_required
def checkout_confirm(request, not_id):
    notif_obj = Notification.objects.get(pk=not_id)
    offer_obj = Offer.objects.get(pk=notif_obj.offer_id)
    if request.method == 'POST':
        item_obj = ItemForSale.objects.get(pk=offer_obj.item_id)
        notif_content = f'"rate_seller"Congratulations on your new {item_obj.name}. Please take the time to rate {item_obj.seller} as a seller.'
        notify(offer_obj, request.user, notif_content, datetime.now())
        clean_checkout_session(request)
        notif_obj.delete()
        notif_obj.save()
        return redirect('inbox', username=request.user.username)
    return render(request, 'users/checkout_confirm.html', context={
        'user_info': request.session['user_info'],
        'user_address': request.session['user_address'],
        'user_payment': request.session['user_payment'],
        'not_id': not_id,
    })


@login_required
def rate_sales(request, username, not_id):
    if username != request.user.username:
        raise Http404()

    notification = Notification.objects.get(pk=not_id)
    if username != request.user.username:
        raise Http404()
    if request.method == 'POST':
        form = RateSeller(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.userid = notification.offer.item.seller
            saved_form.save()
            return redirect('inbox', username=username)
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

def get_object_or_none(table, key):
    try:
        ret_obj = table.objects.get(pk=key)
    except table.DoesNotExist:
        ret_obj = None
    return ret_obj


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
    return HttpResponse("Clean as f*ck boi")

def notify(offer_obj, recipient, content, date_time):
    print(recipient.email)
    send_mail(
        subject="New message from Fyresale",
        message=content[12:] + '\nhttp://localhost:8000/users/' + str(recipient.username) + '/inbox',
        from_email=None,
        recipient_list=[recipient.email],
        fail_silently=False
    )
    new_not = Notification.objects.create(
        recipient=recipient,
        offer=offer_obj,
        content=content,
        timestamp=date_time
    )


def calculate_average(user_obj):
    ratings = User_rating.objects.filter(userid=user_obj)
    count = 0
    sum = 0
    print(ratings)
    if len(ratings) < 1:
        return 0
    for rate in ratings:
        print(rate)
        sum += int(rate.user_rating)
        count += 1
    newsum = sum / 2 #Divide with 2 since the rating is given on a scale form 1-5 whilst user input is 1-10.
    avg_rating = newsum / count 
    return avg_rating
