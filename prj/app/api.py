from typing import List, Optional

from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404

from .models import KebabShop

api = NinjaAPI()


class KebabShopOut(Schema):
    id: int
    name: str
    address: str
    city: str
    opening_hours: str
    email: str
    meat_type: str


class KebabShopIn(Schema):
    name: str
    address: str
    city: str
    opening_hours: str
    email: str
    meat_type: str


def kebab_to_dict(k: KebabShop) -> dict:
    return {
        "id": k.id,
        "name": k.name,
        "address": k.address,
        "city": k.city,
        "opening_hours": k.opening_hours,
        "email": k.email,
        "meat_type": k.meat_type,
    }


@api.get("/kebabshop", response=List[KebabShopOut])
def list_kebabshops(request):
    qs = KebabShop.objects.all()
    return [kebab_to_dict(k) for k in qs]


@api.get("/kebabshop/{kebab_id}", response=KebabShopOut)
def get_kebabshop(request, kebab_id: int):
    k = get_object_or_404(KebabShop, id=kebab_id)
    return kebab_to_dict(k)


@api.post("/kebabshop", response=KebabShopOut)
def create_kebabshop(request, payload: KebabShopIn):
    k = KebabShop.objects.create(**payload.dict())
    return kebab_to_dict(k)


@api.put("/kebabshop/{kebab_id}", response=KebabShopOut)
def update_kebabshop(request, kebab_id: int, payload: KebabShopIn):
    k = get_object_or_404(KebabShop, id=kebab_id)
    for attr, value in payload.dict().items():
        setattr(k, attr, value)
    k.save()
    return kebab_to_dict(k)
