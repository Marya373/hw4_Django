from django.views import View
from shopapp.models import Client, Order
from datetime import datetime, timedelta
from django.views.generic import TemplateView
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

def hello(request):
    return HttpResponse('Привет!')


def get_all_list_order(request,name_client: str):
    client = Client.objects.filter(name=name_client).first()

    orders = Order.objects.filter(client=client).all()

    context = {
        "name_client": name_client,
        "orders": orders
    }

    return render(request, "shopapp/get_all_list_order.html", context)


def for_sort_products_in_ordered(date_time_placing_order: datetime,
                                 what_is_it_compared_to: datetime,
                                 list_products: list,
                                 order: Order):
    if date_time_placing_order >= what_is_it_compared_to:
        for one_product in order.product.all():
            if one_product not in list_products:
                list_products.append(one_product)


def get_list_products_by_customer(request, name_client: str):
    client = Client.objects.filter(name=name_client).first()

    orders = Order.objects.filter(client=client).all()

    current_datetime = datetime.now()

    seven_days_ago = current_datetime - timedelta(days=7)
    thirty_days_ago = current_datetime - timedelta(days=30)
    year_days_ago = current_datetime - timedelta(days=365)
    

    seven_days_ago_list_product: list = []
    thirty_days_ago_list_product: list = []
    year_ago_list_product: list = []

    for order in orders:
        date_time_placing_order: datetime = order.date_time_placing_order.replace(tzinfo=None)

        for_sort_products_in_ordered(list_products=
                                     seven_days_ago_list_product,
                                     date_time_placing_order=
                                     date_time_placing_order,
                                     what_is_it_compared_to=
                                     seven_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     thirty_days_ago_list_product,
                                     date_time_placing_order=
                                     date_time_placing_order,
                                     what_is_it_compared_to=
                                     thirty_days_ago,
                                     order=
                                     order)

        for_sort_products_in_ordered(list_products=
                                     year_ago_list_product,
                                     date_time_placing_order=
                                     date_time_placing_order,
                                     what_is_it_compared_to=
                                     year_days_ago,
                                     order=
                                     order)

    context = {
        "name_client": name_client,
        "products": [
            seven_days_ago_list_product,
            thirty_days_ago_list_product,
            year_ago_list_product
        ]
    }

    return render(request, "shopapp/get_list_products_by_customer.html", context)


def page_not_found(request, exception):
    return render(request, "shopapp/404.html", status=404)
