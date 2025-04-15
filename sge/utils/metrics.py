from django.utils.formats import number_format
from django.db.models import Sum

from typing import Dict
from products.models import Product
from outflows.models import Outflow


def get_products_metrics() -> Dict:
    products = Product.objects.all()

    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    products_metrics = {
        'total_cost_price': number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        'total_selling_price': number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        'total_quantity': total_quantity,
        'total_profit': number_format(total_profit, decimal_pos=2, force_grouping=True)
    }

    return products_metrics


def get_sales_metrics() -> Dict:
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(
        total_products_sold=Sum('quantity')
    )['total_products_sold'] or 0
    total_sales_value = sum(outflow.product.selling_price * outflow.quantity for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.product.cost_price * outflow.quantity for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost

    sales_metrics = {
        'total_sales': total_sales,
        'total_products_sold': number_format(total_products_sold, decimal_pos=0, force_grouping=True),
        'total_sales_value': number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        'total_sales_profit': number_format(total_sales_profit, decimal_pos=2, force_grouping=True)
    }

    return sales_metrics
