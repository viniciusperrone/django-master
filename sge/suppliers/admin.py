from django.contrib import admin

from suppliers.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Supplier, SupplierAdmin)
