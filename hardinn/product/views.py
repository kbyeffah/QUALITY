from itertools import count

from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Product, ProductImage, ProductInfo
from Cart.models import Cart


# class ProductList(ListView):
#     model = Product
#     template_name = "index.html"
#     context_object_name = "product"


class ProductDetail(DetailView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "product"


# def productDetail2(request, product_id):
#     product = Product.objects.get(id=product_id)
#     imageModel = ""
#     product_info = ""

#     if ProductImage.objects.filter(product=product).count():
#         imageModel = ProductImage.objects.filter(product=product).get()

#     if ProductInfo.objects.filter(product=product).count():
#         product_info = ProductImage.objects.filter(product=product).get()

#     relatedProduct = Product.objects.raw('SELECT * FROM product_product WHERE  name  LIKE  %s limit 2', [product.name])

#     # relatedProduct = Product.objects.filter(name=product.name)
#     for pro in relatedProduct:
#         print(pro)
#     context = {"def_product": product, "imagelist": imageModel, 'related': relatedProduct, 'product_info': product_info}
#     return render(request, "product/show.html", context)


def ProductList(request):
    phones = Product.objects.filter(category="Phone")
    laptop = Product.objects.filter(category="Laptop")
    Tv = Product.objects.filter(name="Tv")
    context = {"Phone": phones, "Laptop": laptop, "Tv": Tv}
    phones = Product.objects.all()
    if request.user.is_authenticated:
        Added_cart = Cart.objects.filter(user=request.user).count()
        request.session['cart'] = Added_cart
        request.session.modified = True
        return render(request, "index.html", context)
    else:

        request.session['cart'] = 0
        return render(request, "index.html", context)
    

def ProductDetail(request, product_id):
    ProductDetail = Product.objects.get(id = product_id)  


def ProductImage(request,product_id):
    ProductImage = Product.objects.get(id = product_id)