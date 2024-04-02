from django.shortcuts import render, HttpResponse
from .models import Produk

# Create your views here.
def index(request):
    title = {'title': 'Beranda'}
    return render(request, "index.html", title)
def katalog(request):
    produk = Produk.objects.all()
    return render(request, "katalog.html", {'title': 'Katalog','katalog': produk})
def tentangkami(request):
    title = {'title': 'Tentang Kami'}
    return render(request, "tentangkami.html", title)
