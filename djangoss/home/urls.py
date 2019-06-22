from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('page2', views.process_datapage2),
    path('page1', views.process_datapage1),
    path('sortbl', views.sort_pricebl),
    path('sortlb', views.sort_pricelb),
    path('sortbl2', views.sort_pricebl2),
    path('sortlb2', views.sort_pricelb2),
    path('<int:id_product>', views.find),
]
