from . models import Cart,CartItem
from . views import _Cart_id

def Counter(request):
    Item_Count = 0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            cart=Cart.objects.filter(Cart_id=_Cart_id(request))
            Cat_Items=CartItem.objects.all().filter(Cart=cart[:1])
            for Cart_Item in Cat_Items:
                Item_Count += Cart_Item.Quantity
        except Cart.DoesNotExist:
            Item_Count = 0
    return dict(Item_Count=Item_Count)