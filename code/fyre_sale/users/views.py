from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import SignInForm, SignUpForm, PaymentInsert, AddressInsert
from users.models import User
from items.models import Offer


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


def profilepage(request):
    return render(request, 'frontpage/index.html')


def inbox(request, params=None):
    user = User.objects.get(username=request.user)
    if params == 'my_bids':
        offers = Offer.objects.filter(buyer_id=user.id)
        return render(request, 'users/inbox.html', context={
            'user': user,
            'offers': offers
        })
    elif params == 'my_items':
        bids = Offer.objects.raw("""
            SELECT * FROM items_offer O WHERE O.item_id IN (
              SELECT I.id FROM items_itemforsale I WHERE I.seller_id = %s
            )
            """, [user.id]
        )
        return render(request, 'users/inbox.html', context={
            'user': user,
            'bids': bids,
        })
    notifications = [
        {
            "id": 1,
            "title": "Bid rejected.",
            "date": "2022-05-08",
            "time": "12:35:22",
            "content": "Ravisson Travis rejected your bid on item \"Cool shirt\""
        },
        {
            "id": 2,
            "title": "Bid rejected.",
            "date": "2022-05-08",
            "time": "18:25:52",
            "content": "John Doe rejected your bid on item \"Video game collection\""
        },
        {
            "id": 3,
            "title": "Bid accepted.",
            "date": "2022-05-09",
            "time": "12:46:55",
            "content": "Jane Johnson accepted your bid on item \"Cool shirt\""
        }
    ]
    return render(request, 'users/inbox.html', context={
        'user': user,
        'notifications': notifications
    })


def notifications(request, not_id):
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
            return redirect('user_page')
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
            user_id.save()
        return redirect('user_page')
    else:
        form = AddressInsert(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'users/address.html', {
        'form': form
    })