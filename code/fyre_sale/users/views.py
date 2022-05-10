from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm, PaymentInsert, AddressInsert
from .models import User
from items.models import Offer
from django.contrib.formtools.wizard.views import SessionWizardView


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
                                 "SELECT I.id FROM items_itemforsale I WHERE I.seller_id = %s)\n", [user.id])
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

class Checkout(SessionWizardView):
    template_name = 'checkout.html'
    def done(self, form_list, **kwargs):
        form_data = self.process_form_data(form_list)
        return self.render_to_response('done.html', {'form_data': form_data})

    def process_form_data(form_list):
        form_data = [form.cleaned_data for form in form_list]
        return form_data

