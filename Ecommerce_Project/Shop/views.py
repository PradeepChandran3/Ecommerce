from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from.models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def AllProductCategory(request,C_Slug=None):
    C_Page=None
    Product_list=None
    if C_Slug!=None:
        C_Page=get_object_or_404(Category,Slug=C_Slug)
        Product_List=Product.objects.all().filter(Category=C_Page,Available=True)
    else:
        Product_List=Product.objects.all().filter(Available=True)
    paginator=Paginator(Product_List,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        Products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        Products=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'Category':C_Page,'Products':Products})

def ProductDetail(request,C_Slug,Product_Slug):
    try:
        product=Product.objects.get(Category__Slug=C_Slug,Slug=Product_Slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'Product':product})

