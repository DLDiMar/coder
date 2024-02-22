from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Checkout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def checkout_view(request):
    if request.method == 'POST':
        user = request.user
        payment_type = request.POST['payment_type']
        third_party_pay_plugin = request.POST['third_party_pay_plugin']
        amount = request.POST['amount']
        checkout = Checkout(user=user, payment_type=payment_type, third_party_pay_plugin=third_party_pay_plugin, amount=amount)
        checkout.save()
        return redirect('thank_you')
    return render(request, 'checkout.html')

def thank_you_view(request):
    return render(request, 'thank_you.html')

def bad_redirect(request):
    return render(request, 'bad_redirect.html')