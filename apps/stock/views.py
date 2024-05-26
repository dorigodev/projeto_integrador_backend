from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from apps.stock.models import Product
from apps.stock.forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    products = Product.objects.filter(available=True).filter(user=request.user)

    products_count = products.count()

    product_instock = []
    for product in products:
        instock = product.get_instock()
        product_instock.append(instock)
    product_instock = sum(product_instock)

    product_pricestock = []
    for product in products:
        instock = product.get_instock()
        prices = product.get_price()
        new_price = instock * prices
        product_pricestock.append(new_price)
    product_pricestock = round(sum(product_pricestock), 2)
    return render(request, 'stock_templates/index.html', {'products': products,
                                                          'products_count': products_count,
                                                          'product_stock_numbers': product_instock,
                                                          'product_priceStock': product_pricestock})


# Create
@csrf_exempt
def create_product(request):
    form = ProductForm()
    products = Product.objects.filter(available=True).filter(user=request.user)
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged')
        return redirect("login")
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto cadastrado com sucesso')
            return redirect("index")
    return render(request, 'stock_templates/create_product.html', {'form': form, 'products': products})


# Read
def read_product(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    product_object = get_object_or_404(Product, pk=product_id)
    products = Product.objects.filter(available=True).filter(user=request.user)
    return render(request, 'stock_templates/product.html', {'products': products,'product': product_object, })


# Update
@csrf_exempt
def update_product(request, product_id):
    product_object = Product.objects.get(id=product_id)
    form = ProductForm(instance=product_object)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product_object)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado com sucesso')
            return redirect("index")

    return render(request, 'stock_templates/update_product.html', {'form': form, 'product': product_object,
                                                                   'product_id': product_id})


# Delete
@csrf_exempt
def delete_product(request, product_id):
    product_object = Product.objects.get(id=product_id)
    product_object.delete()
    messages.success(request, 'Producto deletado com sucesso')
    return redirect("index")


def search_product(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado")
        return redirect("login")
    products = Product.objects.filter(user=request.user)
    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            products = Product.objects.filter(name__icontains=search)

    products_count = products.count()

    product_instock = []
    for product in products:
        instock = product.get_instock()
        product_instock.append(instock)
    product_instock = sum(product_instock)

    product_pricestock = []
    for product in products:
        instock = product.get_instock()
        prices = product.get_price()
        new_price = instock * prices
        product_pricestock.append(new_price)
    product_pricestock = sum(product_pricestock)

    return render(request, 'stock_templates/index.html', {'products': products, 'products_count': products_count,
                                                          'product_stock_numbers': product_instock,
                                                          'product_priceStock': product_pricestock})

