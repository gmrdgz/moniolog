from django.urls import path
from wallets import views

urlpatterns = [
    path('', views.wallets, name='wallets'),
    path('new/', views.new_wallet, name='new_wallet')
]
