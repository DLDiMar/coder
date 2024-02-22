from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(_('email address'))
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    sso_id = models.CharField(max_length=128, blank=True)

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=128)
    third_party_pay_plugin = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)