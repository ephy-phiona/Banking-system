# from re import U
from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_thirdparty, register_transaction, register_wallet, register_reward

urlpatterns=[
    path("register/",register_customer, name="registration"),
    path("wallet/",register_wallet, name="register"),
    path("currency/",register_currency, name="register_1"),
    path("transaction/",register_transaction, name="register_2"),
    path("reward/",register_reward, name="register_3"),
    path("loan/",register_loan, name="register_4"),
    path("notification/",register_notification, name="register_5"),
    path("account/",register_account, name="register_6"),
    path("thirdparty/",register_thirdparty, name="register_7"),
    path("card/",register_card, name="register_8"),
]