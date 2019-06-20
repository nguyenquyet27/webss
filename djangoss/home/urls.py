from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('sortbl', views.sort_pricebl),
    path('sortlb', views.sort_pricelb),
    #thegioididong
    path('tgdd', views.searchtgdd_dis),
    path('tgddbl', views.sortpptgdd_pricebl),
    path('tgddlb', views.sortpptgdd_pricelb),
    #fptshop
    path('fpt', views.searchfpt_dis),
    path('fptbl', views.sortppfpt_pricebl),
    path('fptlb', views.sortppfpt_pricelb),
    #hoanghamobile
    path('hh', views.searchhh_dis),
    path('hhbl', views.sortpphh_pricebl),
    path('hhlb', views.sortpphh_pricelb),
    #vienthonga
    path('vta', views.searchvta_dis),
    path('vtabl', views.sortppvta_pricebl),
    path('vtalb', views.sortppvta_pricelb),
    #mainnguyen
    path('mn', views.searchmn_dis),
    path('mnbl', views.sortppmn_pricebl),
    path('mnlb', views.sortppmn_pricelb),
    #find_id
    path('<int:id_product>', views.find),
]