import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, *[os.pardir]*3)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopify.settings'

import django
django.setup()
import json
from django.contrib.auth.models import User
from customer.models import Customer, Address

filepath = './dummy-data/'

# Load and import customers
with open(filepath + 'customer.json') as jsonfile:
    customers = json.load(jsonfile)
    for cust in customers:
        existUser = User.objects.filter(email=cust['email']).first()
        if existUser is None:
            user = User.objects.create_user(
                username=cust['email'], email=cust['email'],
                password=cust['password'],
                first_name=cust['first_name'],
                last_name=cust['last_name']
            )
            existCust = Customer.objects.filter(user=user).first()
            if existCust is None:
                Customer.objects.create(
                    user=user, created_at=cust['created_at'],
                    updated_at=cust['created_at'],
                    currency=cust['currency'],
                    phone=cust['phone'],
                    verified_email=cust['verified_email'],
                    send_email_welcome=cust['send_email_welcome']
                )

# Load and import addresses
with open(filepath + 'address.json') as jsonfile:
    addresses = json.load(jsonfile)
    for num, adr in enumerate(addresses):
        addrExist = Address.objects.filter(id=num+1).first()
        if addrExist is None:
            Address.objects.create(
                customer_id=adr['customer'],
                address1=adr['address1'],
                address2=adr['address2'],
                city=adr['city'],
                province=adr['province'],
                country=adr['country'],
                company=adr['company'],
                phone=adr['phone'],
                zip=adr['zip'],
                default=adr['default']
            )
