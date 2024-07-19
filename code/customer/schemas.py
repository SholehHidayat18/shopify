from ninja import Schema, ModelSchema, FilterSchema, Field 
from datetime import datetime
from typing import Optional, List, Self 
from pydantic import model_validator

from customer.models import Customer, Address


class AddressIn(Schema):
    Customer_id :int
    address1: str
    address2: Optional[str] = ''
    city: str
    first_name: Optional[str] = ''
    last_name: Optional[str] = ''
    phone: Optional[str] = ''
    province: str
    country: str
    zip: str
    company: str
    name: Optional[str] = ''


class AddressOut(Schema):
    id: int
    Customer_id: int
    first_name: str = Field(alias='customer.user.first_name')
    last_name: str  = Field(alias='customer.user.last_name')
    company: str
    address1: str
    address2: str
    city: str
    province: str
    country: str
    zip: str
    phone: Optional[str] = ''
    name: str
    default: bool

class AddressResp(Schema):
    customer_address: AddressOut

class CustomerOut (Schema):
    id: int
    email: str = Field(alias='user.email')
    created_at: datetime
    updated_at: datetime
    first_name: str = Field(alias='user.first_name')
    last_name: str = Field(alias='user.last_name')
    order_counts: int 
    state: str
    verified_email: bool
    currency: str 
    phone: str
    addresses: OptionalList[AddressOut] = Field(alias='address_set')

class CustomerResp(Schema):
    customer: List[CustomerOut]