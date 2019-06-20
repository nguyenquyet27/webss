from django.shortcuts import render
from django.http import HttpResponse
from . import process
from . import fdis

# Create your views here.
def index(request):
    return render(request, 'pages/search.html')


def process_data(request):
    x = request.POST.get("chuoi")
    kq = process.process_search(x)
    return render(request,'pages/search.html',kq)

def sort_price(request):
    kq = process.sort()
    return render(request,'pages/search.html',kq)
#masp


def fsp(request):
    y = "dt"
    kq = fdis.find_masp(y)
    return render(request,'pages/masp.html',kq)

def fsptab(request):
    y = "tab"
    kq = fdis.find_masp(y)
    return render(request,'pages/masp.html',kq)

def fsplt(request):
    y = "lt"
    kq = fdis.find_masp(y)
    return render(request,'pages/masp.html',kq)

#distributor
def dis_tgdd(request):
    y = "thegioididong"
    kq = fdis.find_distributor(y)
    return render(request,'pages/distributor.html',kq)

def dis_fpt(request):
    y = "fptshop"
    kq = fdis.find_distributor(y)
    return render(request,'pages/distributor.html',kq)

def dis_hh(request):
    y = "hoanghamobile"
    kq = fdis.find_distributor(y)
    return render(request,'pages/distributor.html',kq)

def dis_vta(request):
    y = "vienthonga"
    kq = fdis.find_distributor(y)
    return render(request,'pages/distributor.html',kq)

def dis_mn(request):
    y = "mainguyen"
    kq = fdis.find_distributor(y)
    return render(request,'pages/distributor.html',kq)
#find_id
def find(request, id_product):
    kq = process.find_id(id_product)
    return render(request,'pages/product.html',kq) 