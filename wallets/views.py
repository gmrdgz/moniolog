from django.shortcuts import render, redirect
from .models import Wallet
from .forms import NewWallet


def wallets(request):
    if request.method == 'GET':
        wallets = Wallet.objects.all()
        return render(request, 'wallets.html', {'wallets': wallets})
    elif request.method == 'POST':
        Wallet.objects.create(bank_name=request.POST['bank_name'], account_code=request.POST['account_code'])
        return redirect('wallets')

def new_wallet(request):
    return render(request, 'new_wallet.html', {'form': NewWallet})
