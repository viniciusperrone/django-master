from typing import Dict
from products.models import Product


def get_products_metrics() -> Dict:
    products = Product.objects.all()

    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    products_metrics = {
        'total_cost_price': total_cost_price,
        'total_selling_price': total_selling_price,
        'total_quantity': total_quantity,
        'total_profit': total_profit
    }

    return products_metrics
