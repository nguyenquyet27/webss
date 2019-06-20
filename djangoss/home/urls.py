from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('sortbl', views.sort_pricebl),
    path('sortlb', views.sort_pricelb),
    #thegioididong
    path('tgdd', views.searchtgdd_dis),
    #fptshop
    path('fpt', views.searchfpt_dis),
    #hoanghamobile
    path('hh', views.searchhh_dis),
    #vienthonga
    path('vta', views.searchvta_dis),
    #mainnguyen
    path('mn', views.searchmn_dis),
    #find_id
    path('<int:id_product>', views.find),
]