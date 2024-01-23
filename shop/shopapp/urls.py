from django.urls import path
from shopapp.views import get_all_list_order, get_list_products_by_customer, hello

app_name = 'shopapp'

urlpatterns = [
    path('get_all_list_order/<name_client>/', get_all_list_order, name='get_all_list_order'),
    path('get_list_products_by_customer/<name_client>/', get_list_products_by_customer, name='get_list_products_by_customer'),
    path('hello/', hello, name='hello'),
]
