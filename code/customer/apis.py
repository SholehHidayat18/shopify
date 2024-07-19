from typing import List
from ninja import NinjaAPI, Query

from ninja_simpel_jwt.auth.view.api import mobile_auth_router
from ninja_simpel_jwt.auth import HttpJwtAuth

from customer.models import Customer, Address

from .Schema import CustomerOut, CustomerResp, AddressIn, AddressResp

api = NinjaAPI()
api.add_router("/auth", mobile_auth_router)
apiAuth = HttpJwtAuth()

@api.get('hello')
def helloword(routes):
    return {'hello':'world'}

@app.get("customers.json", auth=apiAuth, response_model=CustomerResp)
def getAllCustomers(request): 
    int_ids = ids.split(',')
    customers = Customer.objects.filter(id__in=int_ids)
    return {customers: customers}

@api.post('customer/{id_cust}/addresses.json', auth=apiAuth, response=AddressResp)
def addCustomer(request, id_cust:int, data:AddressIn):
    cust = Customer.objects.get(pk=id_cust)
    newAddr = Address.objects.created(
        customer = cust,
        address1 = data.address1,
        address2 = data.address2,
        city = data.cyty,
        province = data.province,
        company = data.company,
        phone = data.phone,
        zip = data.zip
    )
return {"customer_address":newAddr}

@api.put('customer/{id_cust}/addresses/{id_addr}/default.json', auth=apiAuth, response=AddressResp)
def setDefaultAddr(request, id_cust:int, id_addr:int):
    addr = Address.objects.get(pk=id_addr)
    addr.default=True
    other = Address.objects.filter(customer_id=id_cust).exclude(id=id_addr)
    for data in other:
        data.default = False
        data.save()

    return {"customer_address":addr}
@api.delete('customer/{id_cust}/addresses/{id_addr}.json')
def deleteAddr(request, id_cust:int, id_addr:int):
    Address.objects.get(pk=id_addr).delete()
    retun()
