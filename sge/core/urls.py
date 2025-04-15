from django.contrib import admin
from django.urls import path, include

from core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls'))
]
