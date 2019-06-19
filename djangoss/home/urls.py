from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('distributor', views.fdistri),
    path('mobile', views.fsp),
    path('tab', views.fsptab),
    path('laptop', views.fsplt),
    path('<int:id_product>', views.find),
    path('<str:distributor>', views.fdistributor)
]