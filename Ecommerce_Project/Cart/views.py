from django.shortcuts import render, redirect, get_object_or_404
from Shop.models import Product
from.models import  Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist


def _Cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def Add_Cart(request,Product_id):
    product=Product.objects.get(id=Product_id)
    try:
        cart=Cart.objects.get(Cart_id=_Cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            Cart_id=_Cart_id(request)
        )
        cart.save(),
    try:
        Cart_Item=CartItem.objects.get(Product=product,Cart=cart)
        if Cart_Item.Quantity < Cart_Item.Product.Stock:
            Cart_Item.Quantity += 1
        Cart_Item.save()
    except CartItem.DoesNotExist:
        Cart_Item=CartItem.objects.create(
            Product=product,
            Quantity=1,
            Cart=cart
        )
        Cart_Item.save()
    return redirect('Cart:Cart_Detail')

def Cart_Detail (request,total=0,counter=0,Cart_Items=None):
    try:
        cart=Cart.objects.get(Cart_id=_Cart_id(request))
        Cart_Items=CartItem.objects.filter(Cart=cart,Active=True)
        for Cart_Item in Cart_Items:
            total+=(Cart_Item.Product.Price * Cart_Item.Quantity)
            counter +=Cart_Item.Quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(Cart_Items=Cart_Items,total=total,counter=counter))


def Cart_Remove (request,Product_id):
    cart=Cart.objects.get(Cart_id=_Cart_id(request))
    product=get_object_or_404(Product,id=Product_id)
    cart_item=CartItem.objects.get(Product=product,Cart=cart)
    if cart_item.Quantity >1:
        cart_item.Quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart:Cart_Detail')


def Full_Remove (request,Product_id):
    cart=Cart.objects.get(Cart_id=_Cart_id(request))
    product=get_object_or_404(Product,id=Product_id)
    cart_item=CartItem.objects.get(Product=product,Cart=cart)
    cart_item.delete()
    return redirect('Cart:Cart_Detail')