from django.contrib import admin
from apps.stock.models import Product
# Register your models here.


class ListingProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'inStock', 'available')
    list_filter = ('name', 'available')
    search_fields = ('name',)
    list_display_links = ('name',)
    list_editable = ('available',)
    list_per_page = 10


admin.site.register(Product, ListingProductAdmin)
