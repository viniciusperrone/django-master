from django.shortcuts import render
import json

from utils.metrics import get_products_metrics, get_sales_metrics, get_daily_sales_data, get_daily_sales_quantity_data


def home(request):
    products_metrics = get_products_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    daily_sales_quantity_data = get_daily_sales_quantity_data()

    context = {
        'product_metrics': products_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
    }

    return render(request, 'home.html', context)
