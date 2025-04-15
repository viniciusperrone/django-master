from django.shortcuts import render

from utils.metrics import get_products_metrics, get_sales_metrics

def home(request):
    products_metrics = get_products_metrics()
    sales_metrics = get_sales_metrics()

    context = {
        'product_metrics': products_metrics,
        'sales_metrics': sales_metrics
    }

    return render(request, 'home.html', context)
