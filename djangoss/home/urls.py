from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('distributor', views.fdistri),
    path('<str:distributor>', views.fdistributor),
    path('<int:id_product>', views.find)
]