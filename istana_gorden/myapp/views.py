from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    title = {'title': 'Beranda'}
    return render(request, "index.html", title)
def katalog(request):
    title = {'title': 'Katalog'}
    return render(request, "katalog.html", title)
def tentangkami(request):
    title = {'title': 'Tentang Kami'}
    return render(request, "tentangkami.html", title)
