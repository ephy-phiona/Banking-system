from django.shortcuts import render
from .forms import CustomerRegistrationForm, WalletRegistrationForm , CurrencyRegistrationForm,TransactionRegistrationForm,RewardRegistrationForm,LoanRegistrationForm,NotificationsRegistrationForm,AccountRegistrationForm,ThirdPartyRegistrationForm,CardRegistrationForm



# from Wallet.forms import CustomerRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"Wallet/register_wallet.html",{"form":form})

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request,"Wallet/register_currency.html",{"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"Wallet/register_transaction.html",{"form":form})

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"Wallet/register_reward.html",{"form":form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"Wallet/register_loan.html",{"form":form})

def register_notification(request):
    form = NotificationsRegistrationForm()
    return render(request,"Wallet/register_notification.html",{"form":form})    

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"Wallet/register_account.html",{"form":form})    

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"Wallet/register_thirdparty.html",{"form":form}) 

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"Wallet/register_card.html",{"form":form}) 
