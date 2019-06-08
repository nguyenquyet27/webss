from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.process_data),
    path('<int:id_product>', views.test)
]