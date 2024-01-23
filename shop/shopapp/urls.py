from django.urls import path
from shopapp.views import get_all_list_order, get_list_products_by_customer

app_name = 'shopapp'

urlpatterns = [
    path('get_all_list_order/', get_all_list_order, name='get_all_list_order'),
    path('get_list_products_by_customer/', get_list_products_by_customer, name='get_list_products_by_customer'),
]
