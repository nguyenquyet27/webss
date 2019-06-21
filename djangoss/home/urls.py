from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('showmore', views.process_datamore),
    path('sortbl', views.sort_pricebl),
    path('sortlb', views.sort_pricelb),
    path('<int:id_product>', views.find),
]
