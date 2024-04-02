from django.shortcuts import render
from .models import Item
from myapp.models import Produk

# Create your views here.
def items(request, type):
    product=Produk.objects.get(nama__icontains=type)
    data=Item.objects.filter(jenis_produk_id=product.pk)
    return render(request, "productlist.html", {'title':type, 'product':type, 'data': data})
def checkout(request):
    getReq=request.GET.get('id')
    data=Item.objects.get(id__exact=getReq)
    name=data.nama
    return render(request, "checkout.html", {'item': data, 'title':'Checkout','id':getReq, 'name':name})