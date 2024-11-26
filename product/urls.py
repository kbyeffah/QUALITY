from django.urls import path

from .views import ProductList, ProductDetail 
from .views import *

urlpatterns = [
    path("", ProductList, name="product-cart"),
    path("product-detail/<int:product_id>", ProductDetail, name="product"),
    path("productimage/<int:product_id>", ProductImage),
    # path("home/", Home, name="home"),
]
