from django.shortcuts import render
from django.http import HttpResponse
from . import process

# Create your views here.
def index(request):
    return render(request, 'pages/pages1.html')

def process_data(request):
    x = request.POST.get("chuoi")
    kq = process.process_search(x)
    return render(request,'pages/pages1.html',kq) 

def test(request, id_product):
    kq = process.find_id(id_product)
    return render(request,'pages/pages2.html',kq) 