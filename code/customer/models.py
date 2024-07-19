from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT, unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    verified_email = models.BooleanField(default=False)
    send_email_welcome = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=10)

    @property
    def order_counts(self):
        return 0

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=20)
    company = models.CharField(max_length=200)
    default = models.BooleanField(default=False)

    @property
    def name(self):
        return f"{self.customer.user.first_name} {self.customer.user.last_name}"
