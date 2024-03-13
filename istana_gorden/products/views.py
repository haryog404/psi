from django.shortcuts import render

# Create your views here.
def gorden(request):
    data={'title':'Gorden', 'product':'Gorden'}
    return render(request, "productlist.html", data)
def rollet(request):
    data={'title':'Rollet', 'product':'Rollet'}
    return render(request, "productlist.html", data)
def checkout(request):
    getReq=request.GET.get('name')
    data={'title':'Checkout','name':getReq}
    return render(request, "checkout.html", data)