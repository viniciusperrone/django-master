from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from utils.metrics import get_products_metrics

from products.models import Product
from products.serializers import ProductSerializer
from products.forms import ProductForm

from brands.models import Brand
from categories.models import Category


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get("title")
        serie_number = self.request.GET.get("serie_number")
        category = self.request.GET.get("category")
        brand = self.request.GET.get("brand")

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['product_metrics'] = get_products_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'

class ProductCreateListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
