from django.conf.urls.static import static
from django.urls import path
from apps.stock.views import index, read_product, search_product, create_product, update_product, delete_product
from projetoIntegradorBackend import settings

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>', read_product, name='product'),
    path('search_product', search_product, name='search_product'),
    path('create_product', create_product, name='create_product'),
    path('update_product/<int:product_id>', update_product, name='update_product'),
    path('delete_product/<int:product_id>', delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

