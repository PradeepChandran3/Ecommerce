from django.shortcuts import render
from Shop.models import Product
from django.db.models import Q

def SearchResult(request):
    Products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        Products=Product.objects.all().filter(Q(Name__contains=query) | Q(Description__contains=query))
        return render(request,'search.html',{'query':query,'Products':Products})
