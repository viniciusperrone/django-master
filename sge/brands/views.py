from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from brands.models import Brand
from brands.forms import BrandForm


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(LoginRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'

class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
