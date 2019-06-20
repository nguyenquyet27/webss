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
    return render(request,'pages/search.html',kq)

def sort_pricebl(request):
    kq = process.sort_belon()
    return render(request,'pages/search.html',kq)

def sort_pricelb(request):
    kq = process.sort_lonbe()
    return render(request,'pages/search.html',kq)

#distributor
#thegioididong
def searchtgdd_dis(request):
    distributor = "thegioididong"
    kq = process.searchpp(distributor)
    return render(request,'pages/search.html',kq)

def sortpptgdd_pricebl(request):
    distributor = "thegioididong"
    kq = process.sortpp_belon(distributor)
    return render(request,'pages/search.html',kq)

def sortpptgdd_pricelb(request):
    distributor = "thegioididong"
    kq = process.sortpp_lonbe(distributor)
    return render(request,'pages/search.html',kq)
#fptshop
def searchfpt_dis(request):
    distributor = "fptshop"
    kq = process.searchpp(distributor)
    return render(request,'pages/search.html',kq)

def sortppfpt_pricebl(request):
    distributor = "fptshop"
    kq = process.sortpp_belon(distributor)
    return render(request,'pages/search.html',kq)

def sortppfpt_pricelb(request):
    distributor = "fptshop"
    kq = process.sortpp_lonbe(distributor)
    return render(request,'pages/search.html',kq)
#hoanghamobile
def searchhh_dis(request):
    distributor = "hoanghamobile"
    kq = process.searchpp(distributor)
    return render(request,'pages/search.html',kq)

def sortpphh_pricebl(request):
    distributor = "hoanghamobile"
    kq = process.sortpp_belon(distributor)
    return render(request,'pages/search.html',kq)

def sortpphh_pricelb(request):
    distributor = "hoanghamobile"
    kq = process.sortpp_lonbe(distributor)
    return render(request,'pages/search.html',kq)
#vienthonga
def searchvta_dis(request):
    distributor = "vienthonga"
    kq = process.searchpp(distributor)
    return render(request,'pages/search.html',kq)

def sortppvta_pricebl(request):
    distributor = "vienthonga"
    kq = process.sortpp_belon(distributor)
    return render(request,'pages/search.html',kq)

def sortppvta_pricelb(request):
    distributor = "vienthonga"
    kq = process.sortpp_lonbe(distributor)
    return render(request,'pages/search.html',kq)
#mainguyen
def searchmn_dis(request):
    distributor = "mainguyen"
    kq = process.searchpp(distributor)
    return render(request,'pages/search.html',kq)

def sortppmn_pricebl(request):
    distributor = "mainguyen"
    kq = process.sortpp_belon(distributor)
    return render(request,'pages/search.html',kq)

def sortppmn_pricelb(request):
    distributor = "mainguyen"
    kq = process.sortpp_lonbe(distributor)
    return render(request,'pages/search.html',kq)

def find(request, id_product):
    kq = process.find_id(id_product)
    return render(request,'pages/product.html',kq) 