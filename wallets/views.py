from django.shortcuts import render, redirect
from .models import Wallet
from .forms import WalletForm


def wallets(request):
    if request.method == 'GET':
        wallets = Wallet.objects.all()
        return render(request, 'wallets.html', {'wallets': wallets})
    elif request.method == 'POST':
        Wallet.objects.create(bank_name=request.POST['bank_name'], account_code=request.POST['account_code'])
        return redirect('wallets')

def new_wallet(request):
    return render(request, 'new_wallet.html', {'form': WalletForm})

def delete_wallet(request, id):
    if request.method == 'POST':
        wallet = Wallet.objects.get(id=id)
        wallet.delete()
        return redirect('wallets')

def update_wallet(request, id):
    if request.method == 'GET':
        return render(request, 'update_wallet.html', {'form': WalletForm, 'id': id})
    elif request.method == 'POST':
        wallet = Wallet.objects.get(id=id)
        wallet = WalletForm(request.POST, instance=wallet)
        wallet.save()
        return redirect('wallets')
