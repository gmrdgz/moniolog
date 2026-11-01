from django.db import models

class Wallet(models.Model):
    bank_name = models.CharField(max_length=20)
    account_code = models.CharField(max_length=34)
