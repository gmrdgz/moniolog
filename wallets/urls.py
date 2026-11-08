from django.urls import path
from wallets import views

urlpatterns = [
    path('', views.wallets, name='wallets'),
    path('new/', views.new_wallet, name='new_wallet'),
    path('delete/<int:id>', views.delete_wallet, name='delete_wallet'),
    path('update/<int:id>', views.update_wallet, name='update_wallet'),
]
