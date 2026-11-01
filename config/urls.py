
from django.contrib import admin
from django.urls import path, include
from wallets import urls as wallets_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallets/', include(wallets_urls.urlpatterns), name='wallets'),
]
