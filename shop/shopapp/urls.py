from django.urls import path
from shop.shop.shopapp.views import get_all_list_order, get_list_products_by_customer

app_name = 'shopapp'

urlpatterns = [
    path('get_all_list_order/<str:name_client>/',
         get_all_list_order,
         name='get_all_list_order'),
    path('get_list_products_by_customer/<str:name_client>/',
         get_list_products_by_customer,
         name='get_list_products_by_customer'),
]
