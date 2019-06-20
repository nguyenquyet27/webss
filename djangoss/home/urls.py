from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('sort', views.sort_price),
    path('mobile', views.fsp),
    path('tab', views.fsptab),
    path('laptop', views.fsplt),
    path('thegioididong', views.dis_tgdd),
    path('fptshop', views.dis_fpt),
    path('hoanghamobile', views.dis_hh),
    path('vienthonga', views.dis_vta),
    path('mainguyen', views.dis_mn),
    path('<int:id_product>', views.find),
]