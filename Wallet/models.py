from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField(default='') 
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Wallet(models.Model): 
    user_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=13)
    user_email=models.EmailField()
    account_number=models.CharField(max_length=15)
    account_name=models.CharField(max_length=20)
    balance=models.IntegerField()
    amount=models.IntegerField()
    date_created=models.DateTimeField()
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency')
    status=models.CharField(max_length=20)
    pin=models.IntegerField()

class Currency(models.Model):
    country_of_origin = models.CharField(max_length=20)
    symbol=models.CharField(max_length=20)
    amount = models.IntegerField()    

class Transaction(models.Model):
    transaction=models.CharField(max_length=40,)
    wallet=models.ForeignKey(Wallet,on_delete=models. CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=20)
    transaction_charge=models.IntegerField()
    datetime=models.DateTimeField()
    origin_account=models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name="transactions_origin_account", null=True)
    destination_account=models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name="transactions_destination_account", null= True)
    message=models.CharField(max_length=20, null= True)
    TRANSACTION_CHOICES= (
    ('D','Debit'),
    ('C','Credit'),

    )

class Reward(models.Model):
    points=models.BigIntegerField()
    date_of_reward=models.DateTimeField()
    transaction_amount=models.IntegerField()

class Loan(models.Model):
    loan_id=models.CharField(max_length=20)
    loan_type=models.CharField(max_length=20)
    amount=models.IntegerField()
    interest=models.IntegerField()
    loan_term=models.IntegerField()
    payment_due_date=models.DateTimeField()
    loan_balance=models.IntegerField()

class Notifications(models.Model):
    messages= models.TextField()
    title=models.CharField(max_length=20)
    status=models.CharField(max_length=20)   
    recepients=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="notifications_recepients")
    datetime=models.DateTimeField()

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    balance = models.IntegerField()
    name=models.CharField(max_length=20)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='account_wallet')
    ACCOUNTTYPE_CHOICES = (
        ('W','   Withdraw'),
        ('S','   Savings'),
        ('D','   Deposit'),

    )

class ThirdParty(models.Model):
    account = models.ForeignKey('account',on_delete=models.CASCADE,related_name='account_third_party')
    name = models.CharField(max_length=20)
    transaction_cost = models.IntegerField()
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='third_party_currency')
    location=models.CharField(max_length=20)

class Card(models.Model):
    card_number=models.IntegerField(default=False)
    card_name=models.CharField(max_length=30, blank= True)
    card_type=models.CharField(max_length=30, blank= True, default=False)
    expiry_date=models.DateTimeField(default= datetime.datetime.now)
    security_code=models.IntegerField(default= False)
    date_ofissue=models.DateTimeField(default= datetime.datetime.now)
    account_number=models.IntegerField(default= False)

