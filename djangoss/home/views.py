from django.shortcuts import render
from django.http import HttpResponse
from . import process
from . import fdis

# Create your views here.
def index(request):
    return render(request, 'pages/pages1.html')


def process_data(request):
    x = request.POST.get("chuoi")
    kq = process.process_search(x)
    return render(request,'pages/pages1.html',kq)

def sort_price(request):
    kq = process.sort()
    return render(request,'pages/pages1.html',kq)
#masp


def fsp(request):
    y = "dt"
    kq = fdis.find_masp(y)
    return render(request,'pages/pages5.html',kq)

def fsptab(request):
    y = "tab"
    kq = fdis.find_masp(y)
    return render(request,'pages/pages5.html',kq)

def fsplt(request):
    y = "lt"
    kq = fdis.find_masp(y)
    return render(request,'pages/pages5.html',kq)

#distributor
def fdistri(request):
    kq = fdis.name_distributor()
    return render(request, 'pages/pages4.html',kq)

def fdistributor(request, distributor):
    kq = fdis.find_distributor(distributor)
    return render(request,'pages/pages3.html',kq)
#find_id
def find(request, id_product):
    kq = process.find_id(id_product)
    return render(request,'pages/pages2.html',kq) 