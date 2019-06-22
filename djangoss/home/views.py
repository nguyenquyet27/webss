from django.shortcuts import render
from django.http import HttpResponse
from . import process


# Create your views here.
def index(request):
    return render(request, 'pages/search.html')

#all


def process_data(request):
    x = request.POST.get("chuoi")
    kq = process.process_search(x)
    return render(request, 'pages/search.html', kq)

def process_datapage1(request):
    kq = process.process_searchpage1()
    return render(request, 'pages/search.html', kq)


def process_datapage2(request):
    kq = process.process_searchpage2()
    return render(request, 'pages/search.html', kq)

#page1
def sort_pricebl(request):
    kq = process.sort_belon()
    return render(request, 'pages/search.html', kq)


def sort_pricelb(request):
    kq = process.sort_lonbe()
    return render(request, 'pages/search.html', kq)
#page2
def sort_pricebl2(request):
    kq = process.sort_belon2()
    return render(request, 'pages/search.html', kq)


def sort_pricelb2(request):
    kq = process.sort_lonbe2()
    return render(request, 'pages/search.html', kq)


def find(request, id_product):
    kq = process.find_id(id_product)
    return render(request, 'pages/product.html', kq)
