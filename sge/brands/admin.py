from django.contrib import admin
from brands.models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
