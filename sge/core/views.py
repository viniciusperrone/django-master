from django.shortcuts import render

from core.metrics import get_products_metrics

def home(request):
    products_metrics = get_products_metrics()

    context = {
        'product_metrics': products_metrics
    }

    return render(request, 'home.html', context)
